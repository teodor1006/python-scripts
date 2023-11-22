import psutil

# Get the current CPU usage
cpu = psutil.cpu_percent()

# Get the current memory usage
memory = psutil.virtual_memory().percent

# Get the current disk usage
disk = psutil.disk_usage("/").percent

# Get the network activity
# Get the current input/output data rates for each network
io_counters = psutil.net_io_counters(pernic=True)
for interface, counters in io_counters.items():
    print(f"Interface {interface}:")
    print(f" bytes sent: {counters.bytes_sent}")
    print(f" bytes received: {counters.bytes_recv}")

print("#####################################################################################") 

# Get a list of active connections
connections = psutil.net_connections()
for connection in connections:
    print(f"{connection.laddr} <-> {connection.raddr} ({connection.status})")

print("######################################################################################")

# Print the collected data
print(f"CPU usage: {cpu}%")
print(f"Memory usage: {memory}%")
print(f"Disk usage: {disk}%")        