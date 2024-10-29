import socket 
import threading

HOST = "localhost"
PORTA = 50001
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))
servidor.listen()
print("Servidor esperando conexão...")
conexoes = {}
