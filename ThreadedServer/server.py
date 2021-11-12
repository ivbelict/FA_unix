import socket
import threading

def server():
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

p1 = threading.Thread(target=server(), name="t1", args=["1"])
p2 = threading.Thread(target=server(), name="t2", args=["2"])
p1.start()
p2.start()
