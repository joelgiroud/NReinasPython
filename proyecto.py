from tkinter import *#Bibliotecas necesarias 
import tkinter as ttk
from pyswip import Prolog
import socket
import sys

raiz = Tk() # Crea ventana raiz
raiz.title("Problema de las N reinas")
raiz.geometry("450x200+100+100")

frm = ttk.Frame(raiz) # Crea una forma
frm.grid(columnspan=5, rowspan=6, padx=20, pady=20)  # Ajusta los márgenes con padx y pady

img = PhotoImage(file='reina.png') #Imagen reina
img = img.subsample(16) 

ttk.Label(frm).grid(column=5, row=4, padx=10, pady=10)
ttk.Label(frm).grid(column=6, row=5, padx=10, pady=10)

def make_query(elemento: int):
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
        
    # query = f'reinas({elemento}, L).\n' # ESTO ESTA MAL
    query = bytes(f'{elemento}.\n'.encode('ascii'))
        
    try:
        s.sendall(query)
    except socket.error:
        print('Error de comunicación')
    
    responses = []
    
    while True:
        reply = b''
        while True:
            res = s.recv(256)
            reply += res
            if b'\n' in res:
                break
        response_str = reply.decode().strip()
        if response_str == 'no':
            break
        else:
            response_list = eval(response_str)
            responses.append(response_list)

    print(responses)

    s.close()
    return responses
    
def draw_solution(vector, frame):
    for row, col in enumerate(vector, start=1):
        ttk.Label(frame, image=img).grid(column=col, row=row)

def draw_no_solution():
    ttk.Label(frm, text="No se encontró ninguna solución").grid(column=1, row=1)

def draw_solutions(solutions):
    for solution in solutions:
        top = Toplevel(raiz)
        top.title("Solución")
        
        frm_sol = ttk.Frame(top)
        frm_sol.grid(columnspan=5, rowspan=6, padx=20, pady=20)
        
        draw_solution(solution, frm_sol)

def resuelvereinas ():  #ejecuta el programa cuando el boton resolver es presionado y obtiene el num de reinas que dio el usuario
    num_reinas = int(n.get())
    array = make_query(num_reinas)
    if array == []:
        draw_no_solution
    else:
        #for elm in array:
        draw_solutions(array)

# Variable de control
n = ttk.StringVar()

# BOTONES
ttk.Label(frm, text="Número de reinas:").grid(column=7, row=5, padx=5, pady=5, sticky="w") # Etiqueta numero de reinas
ttk.Entry(frm, textvariable=n).grid(column=7, row=6, padx=5, pady=5, sticky="w")

ttk.Button(frm, text="Resolver", command=resuelvereinas).grid(column=4, row=6, padx=5, pady=5, sticky="w") # Boton resolver

ttk.Button(frm,text='Terminar',command=raiz.destroy).grid(column=0, row=6, padx=5, pady=5, sticky="w") # Boton terminar
ttk.Button(frm,text='Minimizar',command=raiz.iconify).grid(column=2, row=6, padx=5, pady=5, sticky="w") # Boton minimizar

raiz.mainloop() # Haz funcionar todo
