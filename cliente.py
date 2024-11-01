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
            self.nome = input("Digite seu nome: ")
            self.cliente.send(self.nome.encode())
            
            threading.Thread(target=self.receber_mensagem).start()
            
            # Chama o método de enviar mensagens
            self.enviar_mensagem()
        except Exception as e:
            print(f"Erro de conexão: {e}")

    def enviar_mensagem(self):
        while True:
            mensagem = input("Você: ")

            # Verifica se o cliente deseja sair
            if mensagem.lower() == '#sair':
                self.cliente.send(mensagem.encode())
                self.cliente.close()
                break
            else:
                self.cliente.send(mensagem.encode())

    def receber_mensagem(self):
        while True:
            try:
                # Recebe mensagens do servidor
                mensagem = self.cliente.recv(1024).decode()
                print(mensagem)
            except Exception as e:
                print(f"Erro ao receber mensagem: {e}")
                self.cliente.close()
                break

if __name__ == "__main__":
    cliente = ClienteChat()  # CLIENTE DEVE COLOCAR O IP DO SERVIDOR
    cliente.conectar()
