import socket
import datetime
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.117', 81))
client_socket.send(('4').encode());
time.sleep(1);
data = client_socket.recv(65536);
data = data.decode()
print (data)
