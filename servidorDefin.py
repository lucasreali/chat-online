import socket 
import threading

HOST = "localhost"
PORTA = 50001

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((HOST, PORTA))
servidor.listen()
print("Servidor esperando conexão...")

conexoes = {}

def gerencCliente(conn):
    while True:
        try:
            mensagem = conn.recv(1024).decode('utf-8')
            if mensagem == "#sair":
                nomeUsu = conexoes.get(conn)
                conn.close()
                broadcast(f"{nomeUsu} saiu do chat!".encode('utf-8'))
                del conexoes[conn]
                break
            else:
                broadcast(mensagem.encode('utf-8'))
        except:
            nomeUsu = conexoes.get(conn)
            conn.close()
            broadcast(f'{nomeUsu} caiu do Chat!')
            del conexoes[conn]

def broadcast(mensagem):
    for conexao in conexoes:
        conexao.send(mensagem)

def iniServer():
    while True: 
        try:
            conn, ender = servidor.accept()
            print(f"Conexão feita com {str(ender)}")

            conn.send('USER'.encode('utf-8'))
            nomeUsu = conn.recv(1024).decode('utf-8')
            conexoes[conn] = nomeUsu

            print(f'Cliente {nomeUsu} se cadastrou')
            boasVindas = f"{nomeUsu} entrou no chat"
            broadcast(boasVindas.encode('utf-8'))
            conn.send('Você se conectou ao Chat! Digite "#sair" para sair do Chat'.encode('utf-8'))

            thread = threading.Thread(target=gerencCliente, args=(conn,))
            thread.start()
        except Exception as ex:
            print(f"Erro de conexão {ex}!")

iniServer()
