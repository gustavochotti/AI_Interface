import tkinter as tk
from tkinter import scrolledtext, messagebox
import google.generativeai as genai
import edge_tts
from datetime import datetime
import asyncio


# Variáveis importantes
API_KEY = "YOUR_API_KEY"  # Sua chave API aqui
AI_MODEL = "gemini-1.5-pro-latest"  # Se deseja, altere o modelo de IA (Verifique os moelos disponíveis executando "models.py")
VOICE = "pt-BR-FranciscaNeural"  # Altere se quiser outra voz (Vozes disponíveis listadas em "voice_list.txt")
USER_NAME = "YOUR_NAME_HERE"  # Seu nome aqui
OUTPUT_TEXT_FILE = f"response_{datetime.now().strftime('%Y%m%d-%H-%M-%S')}.txt"
OUTPUT_AUDIO_FILE = f"audio_{datetime.now().strftime('%Y%m%d-%H-%M-%S')}.mp3"

# Configurar a chave da API do genai
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(AI_MODEL)


# Função para gerar resposta da IA
def gerar_resposta():
    pergunta = input_text.get("1.0", tk.END).strip()
    if not pergunta:
        messagebox.showwarning("Aviso", "Por favor, insira uma pergunta.")
        return

    # Geração da resposta usando o modelo da IA
    try:
        resposta = model.generate_content(pergunta).candidates[0].content.parts[0].text
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, resposta)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar a resposta: {e}")

# Função para limpar os campos de input e output
def nova_pergunta():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Função para exportar a resposta em arquivo .txt
def exportar_texto():
    resposta = output_text.get("1.0", tk.END).strip()
    if not resposta:
        messagebox.showwarning("Aviso", "Nenhuma resposta para exportar.")
        return

    with open(OUTPUT_TEXT_FILE, "w", encoding="utf-8") as file:
        file.write(resposta)
        messagebox.showinfo("Exportado", f"Resposta exportada como {OUTPUT_TEXT_FILE}")

# Função assíncrona para exportar a resposta em arquivo .mp3
async def exportar_audio_async():
    resposta = output_text.get("1.0", tk.END).strip()
    if not resposta:
        messagebox.showwarning("Aviso", "Nenhuma resposta para exportar.")
        return

    try:
        communicate = edge_tts.Communicate(str(resposta).replace("#", "").replace("*", ""), VOICE)
        await communicate.save(OUTPUT_AUDIO_FILE)
        messagebox.showinfo("Exportado", f"Áudio exportado como {OUTPUT_AUDIO_FILE}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao exportar o áudio: {e}")

def exportar_audio():
    asyncio.run(exportar_audio_async())

# Configuração da interface gráfica com Tkinter
root = tk.Tk()
root.title("Interface de IA")
root.geometry("1200x600")
root.configure(bg="#444444")

# Configurar grid para centralizar os elementos
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Título de boas-vindas
welcome_label = tk.Label(root, text=f"Welcome, {USER_NAME}!", font=("Arial", 24), bg="#444444", fg="white")
welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

# Caixa de entrada de texto (Input)
input_label = tk.Label(root, text="Input", font=("Arial", 16, "bold"), bg="#444444", fg="white")
input_label.grid(row=1, column=0, padx=10, sticky="w")
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
input_text.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

# Caixa de saída de texto (Output)
output_label = tk.Label(root, text="Output", font=("Arial", 16, "bold"), bg="#444444", fg="white")
output_label.grid(row=1, column=1, padx=10, sticky="w")
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
output_text.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

# Configurar grid para expandir caixas de texto
root.grid_rowconfigure(2, weight=1)

# Botões
gerar_resposta_button = tk.Button(root, text="Gerar Resposta", font=("Arial", 14), bg="#007bff", fg="white", command=gerar_resposta)
gerar_resposta_button.grid(row=3, column=0, pady=20, sticky="n")

nova_pergunta_button = tk.Button(root, text="Nova Pergunta", font=("Arial", 14), bg="#007bff", fg="white", command=nova_pergunta)
nova_pergunta_button.grid(row=3, column=1, sticky="w", padx=5)

exportar_texto_button = tk.Button(root, text="Exportar Texto", font=("Arial", 14), bg="#007bff", fg="white", command=exportar_texto)
exportar_texto_button.grid(row=3, column=1, padx=5)

exportar_audio_button = tk.Button(root, text="Exportar Áudio", font=("Arial", 14), bg="#007bff", fg="white", command=exportar_audio)
exportar_audio_button.grid(row=3, column=1, sticky="e", padx=5)

root.mainloop()
