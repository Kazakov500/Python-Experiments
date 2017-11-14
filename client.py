import socket




while True:
	sock = socket.socket()
	sock.connect(('localhost', 9090))
	a = input("a: ")
	a = bytes(a, encoding = 'utf-8')
	sock.send(a)
	if not a:
		break

	data = sock.recv(1024)
	sock.close()

	print ("Recived data: ", data)

	D = int(data)
	print ("Converted data: ", D)


#D:\Program\Python\python.exe D:\PyProgs\server.py
#D:\Program\Python\python.exe D:\PyProgs\client.py
