import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)


while True:
    conn, addr = sock.accept()
    print ('+ connected:', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print ('- disconnected:', addr)
            break
        print ("Recived data: ", data)
        a = int(data)
        print ("Converted value: ", a)
        res =  a * a
        print ("Calculated value: ", res)

        conn.send(bytes(str(res), encoding = 'utf-8'))

    conn.close()

#D:\Program\Python\python.exe D:\PyProgs\server.py
#D:\Program\Python\python.exe D:\PyProgs\client.py
