# SSH Honeypot

The SSH honeypot is a simple Python script that simulates an SSH server to capture and log attempted login credentials from potential attackers. It is designed to act as a decoy server, attracting unauthorized login attempts and providing insights into potential security threats.

## Usage

### Installation

1. Clone this repository to your local machine:

```
https://github.com/YoTi1412/HoneyPot.git
```


2. Navigate to the project directory:

```
cd HoneyPot
```


### Running the Honeypot

1. Start the SSH honeypot server:

```
python3 honeypot.py
```


2. The honeypot will begin listening on port 2222 for incoming SSH connections.

3. Connect to the honeypot using an SSH client (e.g., OpenSSH):

```
ssh 127.0.0.1 -p 2222
```

4. You can now interact with the honeypot as if it were an SSH server. Any attempted login credentials (username and password) will be printed to the console.

5. To disconnect from the honeypot, type `exit` or use the `Ctrl + D` keyboard shortcut.

### Configuration

By default, the honeypot uses a simple authentication method that rejects all login attempts and logs the provided username and password. For more advanced configurations, you can modify the `SSHServer` class in the `honeypot.py` script to simulate different behaviors or responses.
