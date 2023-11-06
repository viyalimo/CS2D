import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("IP адрес компьютера:", ip_address)