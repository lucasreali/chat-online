import socket
import threading

class ServidorChat:
    def __init__(self, host='localhost', port=5001):
        self.host = host
        self.port = port
        self.clientes = {}
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.bind((self.host, self.port))
        self.servidor.listen(5)
        print(f"Servidor iniciado em {self.host}:{self.port}")

    def iniciar_servidor(self):
        while True:
            cliente_socket, endereco = self.servidor.accept()
            threading.Thread(target=self.gerenciar_cliente, args=(cliente_socket,)).start()

    def gerenciar_cliente(self, cliente_socket):
        try:
            nome = cliente_socket.recv(1024).decode()
            self.clientes[cliente_socket] = nome
            print(f"{nome} se conectou ao servidor.")

            self.enviar_broadcast(f"{nome} entrou no chat.", cliente_socket)

            while True:
                mensagem = cliente_socket.recv(1024).decode()
                if mensagem.lower() == 'sair':
                    self.remover_cliente(cliente_socket)
                    break
                elif mensagem.startswith("/"):
                    self.enviar_unicast(mensagem, cliente_socket)
                else:
                    mensagem_formatada = f"{nome}: {mensagem}"
                    print(mensagem_formatada)
                    self.enviar_broadcast(mensagem_formatada, cliente_socket)
        except Exception as e:
            print(f"Erro com cliente: {e}")
            self.remover_cliente(cliente_socket)

    def enviar_broadcast(self, mensagem, cliente_socket):
        for cliente in self.clientes:
            if cliente != cliente_socket:
                try:
                    cliente.send(mensagem.encode())
                except Exception as e:
                    print(f"Erro ao enviar mensagem: {e}")
                    self.remover_cliente(cliente)

    def enviar_unicast(self, mensagem, cliente_socket):
        try:
            _, conteudo = mensagem.split("/", 1)
            destinatario_nome, conteudo = conteudo.split(" ", 1)
            remetente_nome = self.clientes[cliente_socket]
            mensagem_formatada = f"[Privado] {remetente_nome}: {conteudo}"
            
            destinatario_socket = None
            for sock, nome in self.clientes.items():
                if nome == destinatario_nome:
                    destinatario_socket = sock
                    break
            
            if destinatario_socket:
                destinatario_socket.send(mensagem_formatada.encode())
            else:
                cliente_socket.send(f"Usuário {destinatario_nome} não encontrado.".encode())
        except ValueError:
            cliente_socket.send("Formato de mensagem inválido. Use: /nomedodestinatario mensagem".encode())

    def remover_cliente(self, cliente_socket):
        if cliente_socket in self.clientes:
            nome = self.clientes[cliente_socket]
            cliente_socket.close()
            del self.clientes[cliente_socket]
            print(f"{nome} saiu do chat.")
            self.enviar_broadcast(f"{nome} saiu do chat.", cliente_socket)

if __name__ == "__main__":
    servidor = ServidorChat()
    servidor.iniciar_servidor()
