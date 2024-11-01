import socket
import threading

HOST = 'localhost'
PORTA = 50001

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORTA))

nomeUsu = input("Escreva um nome para seu usuário: ")

def receber():
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            if mensagem == "USER":
                cliente.send(nomeUsu.encode('utf-8'))
            else:
                print(mensagem)
        except:
            print(f"Você caiu do chat!")
            cliente.close()
            break

def escrever():
    while True:
        mensagem = f"{nomeUsu}: {input("")}"
        cliente.send(mensagem.encode('utf-8'))

threadReceber = threading.Thread(target=receber)
threadEscrever = threading.Thread(target=escrever)
threadReceber.start()
threadEscrever.start()