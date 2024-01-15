import socket
import sys

host = 'localhost'
port = 50000
s = None

print('Creando socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('No se pudo crear el socket')
    sys.exit()

print('Intentando obtener la dirección IP')
try:
    rip = socket.gethostbyname(host)
except socket.gaierror:
    print(f'No se encontró la dirección IP de {host}')
    sys.exit()

print('Conectándose al servidor')
try:
    s.connect((rip, port))
    print('Éxito al conectar al servidor')
except socket.error:
    print('Error al conectar al servidor')
    sys.exit()

elemento = int(input('Elemento: '))
# query = f'reinas({elemento}, L).\n' # ESTO ESTA MAL
query = bytes(f'{elemento}.\n'.encode('ascii'))

try:
    s.sendall(query)
except socket.error:
    print('Error de comunicación')

reply = b''
while True:
    res = s.recv(256)
    reply += res
    if b'\n' in res:
        break

print(reply.decode())

fin = '[].\nfin.\n'
s.sendall(fin.encode('ascii'))
res = s.recv(256)
print(res.decode())

s.close()
