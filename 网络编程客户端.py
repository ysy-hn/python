import socket
s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
print(s.recv(1024))
#
# from urllib.request import urlopen
# webpage = urlopen('http:\\www.python.org')
#
# import re
# text = webpage.read()
# m = re.search(b'<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)
# m.group()


