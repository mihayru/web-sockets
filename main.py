import socket
URLS = {
    '/':'hello index',
    '/blog': 'hello blog'
}

def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method,url)


def generate_headers(method,url):
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n',405)
    if not url in URLS:
        return ('HTTP/1.1 404 Method not allowed\n\n',404)

    return('HTTP/1.1 200 OK\n\n',200)


def generate_content(code,url):
    if code == 404:
        return '<h1>404</h1><p>NOT FOUND</p>'
    if code == 405:
        return '<h1>405</h1><p>METHOD NOT ALLOWED</p>'
    return 
    


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method,url)
    body = generate_content(code, url)

    return (headers + 'hello world').encode()


    


def run():
    #server_socket - это субьект который принимает запрос
    #AF_INET - глобальная переменная AF(AdressFamily)
    #INET - Это сам протокол IP который бывает двух версий iPv4 and iPv6
    #SOCK_STREAM - это TCP
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #SOL_SOCKET - это указание на наш сокет тоесть server_socket.
    #SO_REUSEADDT - переипользовать аддрес(допустить повтроное использование аддреса)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    #Свзязываем этот субьек с конкретным аддресом и портом.
    #bind- принимает кортеж
    server_socket.bind(('127.0.0.1',8000))
    
    #Даем указания серверу чтобы он начал прослушивать свой порт
    server_socket.listen()
    
    #Поскольку мы не знаем сколько будет длиться сессия с клиентом мы исп. бесконечный цикл
    while True:
        #Метод accept() - получает кортеж, нам нужно его распаковать и посмотреть что там пришло
        client_socket,addr = server_socket.accept()
        #Смотрим запрос (1024)-колово байт
        request = client_socket.recv(1024)
        print(request)
        print()
        print(addr)


        response = generate_response(request.decode('utf-8'))
        #Отвечаем клиенту
        #Сокеты не понимают строк они принимают байты поетмоу кодируем строку .encode()
        client_socket.sendall('Hello world'.encode())

        #Мы в браузере ниченго не увидим пока не закроем соединение
        client_socket.close()



#Если мы в консоли визываем main то оно запускае приложени
if __name__ =='__main__':
    run()