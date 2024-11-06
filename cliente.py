import socket
import threading

class ClienteChat:
    # TODO: Adcionar comentarios em todo o codigo para facilitar a apresentação

    def __init__(self, host='localhost', port=5001):
        self.host = host # Endereço do servidor
        self.port = port # Porta usada para a conexão com o servidor.

        # Cria um socket TCP/IP.
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):

        try:
            # Faz a coneção com o servidor
            self.cliente.connect((self.host, self.port))
            print("Conectado ao servidor")

            # Envia nome do usuario para o servidor
            self.cliente.send(self.nome.encode())
            
            threading.Thread(target=self.receber_mensagem).start()
            
            # Chama o método de enviar mensagens
            self.enviar_mensagem()
        except Exception as e:
            print(f"Erro de conexão: {e}")

    def enviar_mensagem(self, mensagem):
        if mensagem.lower() == '#sair':
            self.cliente.send(mensagem.encode())
            self.cliente.close()
        else:
            self.cliente.send(mensagem.encode())

    def receber_mensagem(self):
        try:
            mensagem = self.cliente.recv(1024).decode()
            return mensagem
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")
            return None

