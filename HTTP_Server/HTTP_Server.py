from http.server import HTTPServer, CGIHTTPRequestHandler

print("Starting Server...")

server_address = ("", 8000)#Адрес сервера
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)#Создаем экземпляр
httpd.serve_forever()#Старт