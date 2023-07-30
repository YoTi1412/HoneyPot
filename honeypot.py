import socket
import paramiko
import threading


class SSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username: str, password: str) -> int:
        print(f"{username}:{password}")
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username: str) -> str:
        return 'password'

    def check_channel_request(self, kind: str, chanid: int) -> int:
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def open_session(self, channel):
        self.channel = channel

    def get_allowed_auths(self, username):
        return "password"

    def exec_command(self, command):
        response = f"Command '{command}' not found.\n"
        self.channel.send(response.encode())

    def handle_data(self, data):
        command = data.strip().decode()
        if command.lower() in ["exit", "quit"]:
            self.channel.send("Goodbye!\n".encode())
            self.channel.close()
        else:
            self.exec_command(command)


def handle_connection(client_sock):
    print("New connection received.")
    transport = paramiko.Transport(client_sock)
    server_key = paramiko.RSAKey.from_private_key_file(
        '/Users/info/Desktop/Project/HoneyPot/key')
    transport.add_server_key(server_key)
    ssh = SSHServer()
    transport.start_server(server=ssh)

    try:
        transport.join()
    finally:
        transport.close()


def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('', 2222))
    server_sock.listen(223)

    print("HoneyPot is listening on port 2222...")

    while True:
        client_sock, client_addr = server_sock.accept()
        print(f"Connection from {client_addr[0]}:{client_addr[1]}")
        t = threading.Thread(target=handle_connection, args=(client_sock,))
        t.start()


if __name__ == "__main__":
    main()
