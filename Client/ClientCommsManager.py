import math
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_addr = ('127.0.0.1', 8080)
client.connect(host_addr)
print('Connected to', host_addr)

data = client.recv(1024).decode()
print(data)


client.send('GET|||/Users/yocha/Python Stuff/www/R8.jpg'.encode())

file_size = client.recv(1024).decode()
print(file_size, "bytes")

finished = False
index = 0
file_contents = b""

while not finished:
    data = client.recv(1024)

    index += 1
    print("received data", index, "/", math.ceil(int(file_size)/1024))

    if data.endswith(b"||| END |||"):
        finished = True
        file_contents += data[:-11]
    else:
        file_contents += data

print("finished receiving data")

path_for_new_file = '/Users/yocha/Downloads/'
with open(f"{path_for_new_file}R8.jpg", 'wb') as file:
    file.write(file_contents)

print("finished writing data")

client.close()

