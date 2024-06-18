import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
import os
from plyer import notification

def selecionar_arquivos():
    arquivos = filedialog.askopenfilenames(title="Selecionar arquivos CSV", filetypes=[("Arquivos CSV", "*.csv")])
    if arquivos:
        input_var.set("\n".join(arquivos))
        botao_converter.configure(state="normal")

def selecionar_pasta():
    pasta = filedialog.askdirectory(title="Selecionar local de salvamento")
    if pasta:
        output_var.set(pasta)

def converter_arquivos():
    arquivos = input_var.get().split("\n")
    pasta_salvar = output_var.get()
    
    if not arquivos or not pasta_salvar:
        messagebox.showerror("Erro", "Por favor, selecione arquivos e uma pasta de destino.")
        return
    
    for arquivo in arquivos:
        try:
            df = pd.read_csv(arquivo, delimiter=',')
            nome_arquivo = os.path.splitext(os.path.basename(arquivo))[0]
            caminho_salvar = os.path.join(pasta_salvar, f"{nome_arquivo}_corrigido.xlsx")
            df.to_excel(caminho_salvar, index=False, engine='openpyxl')
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao converter {arquivo}\nErro: {e}")
            return
    
    # Verifica se a aplicação está em foco
    if root.focus_get() is None:
        # Mostra uma notificação do sistema
        notification.notify(
            title="Conversão Concluída",
            message="Todos os arquivos selecionados foram convertidos para Excel.",
            timeout=10
        )
    else:
        # Mostra uma mensagem na tela
        messagebox.showinfo("Conversão Concluída", "Todos os arquivos selecionados foram convertidos para Excel.")

# Cria a janela principal da aplicação
root = ctk.CTk()
root.title("Conversor de CSV para Excel")
root.geometry("600x400")

input_var = ctk.StringVar()
output_var = ctk.StringVar()

# Seleção de arquivos de entrada
label_input = ctk.CTkLabel(root, text="Selecionar arquivos")
label_input.pack(pady=5)

input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10)

input_entry = ctk.CTkEntry(input_frame, textvariable=input_var, width=400)
input_entry.pack(side="left", padx=10)

input_button = ctk.CTkButton(input_frame, text="Procurar", command=selecionar_arquivos)
input_button.pack(side="right")

# Seleção da pasta de saída
label_output = ctk.CTkLabel(root, text="Selecionar local de salvamento")
label_output.pack(pady=5)

output_frame = ctk.CTkFrame(root)
output_frame.pack(pady=10)

output_entry = ctk.CTkEntry(output_frame, textvariable=output_var, width=400)
output_entry.pack(side="left", padx=10)

output_button = ctk.CTkButton(output_frame, text="Procurar", command=selecionar_pasta)
output_button.pack(side="right")

# Botão de conversão
botao_converter = ctk.CTkButton(root, text="Converter", command=converter_arquivos, state="disabled")
botao_converter.pack(pady=20)

# Inicia a aplicação
root.mainloop()
