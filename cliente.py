import socket
import threading

class ClienteChat:
    # TODO: Adcionar comentarios em todo o codigo para facilitar a apresentação

    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):
        try:
            self.cliente.connect((self.host, self.port))
            print("Conectado ao servidor")
            
            self.nome = input("Digite seu nome: ")
            self.cliente.send(self.nome.encode())
            
            threading.Thread(target=self.receber_mensagem).start()

            self.enviar_mensagem()
        except Exception as e:
            print(f"Erro de conexão: {e}")

    def enviar_mensagem(self):
        while True:
            mensagem = input("Você: ")
            if mensagem.lower() == 'sair':
                self.cliente.send(mensagem.encode())
                self.cliente.close()
                break
            else:
                self.cliente.send(mensagem.encode())

    def receber_mensagem(self):
        while True:
            try:
                mensagem = self.cliente.recv(1024).decode()
                print(mensagem)
            except Exception as e:
                print(f"Erro ao receber mensagem: {e}")
                self.cliente.close()
                break

if __name__ == "__main__":
    cliente = ClienteChat()
    cliente.conectar()
