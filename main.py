import tkinter as tk
import cliente

a = cliente.ClienteChat()

screen = tk.Tk()
screen.title("Chat online")
screen.geometry("500x500")

entry = tk.Entry(screen, width=50)
entry.pack(pady=20)  

def enviar_mensagem():
    mensagem = entry.get()
    print("Mensagem enviada:", mensagem)
    entry.delete(0, tk.END)

botao_enviar = tk.Button(screen, text="Enviar", command=enviar_mensagem)
botao_enviar.pack(pady=10)

screen.mainloop()