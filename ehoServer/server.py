import socket

# sock = socket.socket()
# sock.bind(('', 9090))
sock = socket.create_server(('', 9090))
sock.listen(0)
print('working...')
print('listen 0...')
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	if not data:
		break
	msg += data.decode('utf-8')
	conn.send(data)

print(msg)


print('close...')
conn.close()
