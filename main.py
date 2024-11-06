import tkinter as tk
import cliente
import threading

def conectar():
    global cliente_chat
    cliente_chat = cliente.ClienteChat()  # Inserrir IP do servidor
    threading.Thread(target=cliente_chat.conectar).start()
    threading.Thread(target=receber_mensagens).start()

def enviar_mensagem():
    mensagem = entry.get()
    if mensagem:
        text_area.config(state='normal')
        text_area.insert(tk.END, "Você: ", 'você')
        text_area.insert(tk.END, mensagem + "\n")
        text_area.config(state='disabled')
        entry.delete(0, tk.END)
        cliente_chat.enviar_mensagem(mensagem)

def receber_mensagens():
    while True:
        mensagem = cliente_chat.receber_mensagem()
        if mensagem:
            text_area.config(state='normal')
            text_area.insert(tk.END, mensagem + "\n")
            text_area.config(state='disabled')


screen = tk.Tk()
screen.title("Chat online")
screen.geometry("500x500")

text_area = tk.Text(screen, state='disabled', wrap='word', height=22)
text_area.pack(pady=10)

text_area.tag_config('você', foreground='blue')

entry = tk.Entry(screen, width=35)
entry.pack(side=tk.LEFT, padx=(10, 0), pady=10)

botao_enviar = tk.Button(screen, text="Enviar", command=enviar_mensagem, width=10)
botao_enviar.pack(side=tk.LEFT, padx=10, pady=10)

conectar()

screen.mainloop()
