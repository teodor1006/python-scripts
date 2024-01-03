# pip install paramiko
import paramiko

ip_address = "192.168.2.106"
username = "student"
password = "training"

# Create an SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the SSH server
ssh_client.connect(hostname=ip_address, username=username, password=password)
print("Successfully connected to", ip_address)

commands = [
    'cd Desktop; mkdir work',
    'mkdir test_folder'
]

for command in commands:
    stdin, stdout, stderr = ssh_client.exec_command(command)
    print(f"Output for command '{command}':")
    print(stdout.read().decode())
    print("Errors (if any):")
    print(stderr.read().decode())

# Close the SSH connection
ssh_client.close()
