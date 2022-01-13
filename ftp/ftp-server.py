import socket
import os
import shutil
import re


dirname = os.path.join(os.getcwd(), 'docs')


def process(req):
    if req == 'pwd':
        return dirname
    elif req == 'ls':
        return '; '.join(os.listdir(dirname))
    elif req.split()[0] == 'mkdir' and len(req.split()) == 2:
        if not(os.path.exists(req.split()[1])):
            os.mkdir(req.split()[1])
        else:
            return 'такой каталог уже существует'
        return 'создан'
    elif req.split()[0] == 'rmdir' and len(req.split()) == 2:
        if (os.path.exists(req.split()[1])):
            os.rmdir(req.split()[1])
        else:
            return 'нет такого католога'
        return 'удален'
    elif req.split()[0] == 'touch' and len(req.split()) == 2:
        if not(os.path.exists(req.split()[1])):
            text_file = open(req.split()[1], "w")
        else:
            return 'такой файл уже существует'
        return 'файл создан'

    elif req.split()[0] == 'cat' and len(req.split()) == 2:
        if (os.path.exists('docs/' + req.split()[1])):
            file = open('docs/'+req.split()[1])
            text = (file.read())
            file.close()
        else:
            return 'нет такого файла'

        return text

    elif req.split()[0] == 'write' and len(req.split()) == 3:
        if (os.path.exists('docs/' + req.split()[1])):
            file = open('docs/'+req.split()[1])
            text = (file.write(req.split()[2]))
            file.close()
        else:
            return 'нет такого файла'

        return text

    elif req.split()[0] == 'rename' and len(req.split()) == 3:
        if (os.path.exists(req.split()[1])):
            os.rename(req.split()[1], req.split()[2])
        else:
            return 'такого файла не существует'


    return 'bad request'


PORT = 6666

sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
print("Прослушиваем порт", PORT)

while True:
    conn, addr = sock.accept()

    request = conn.recv(1024).decode()
    print(request)

    response = process(request)
    conn.send(response.encode())

conn.close()