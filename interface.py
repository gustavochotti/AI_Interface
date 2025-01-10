import tkinter as tk
from tkinter import scrolledtext, messagebox
import google.generativeai as genai
import edge_tts
from datetime import datetime
import asyncio


# Important variables
API_KEY = "YOUR_API_KEY"  # Your Google AI API key here
AI_MODEL = "gemini-1.5-pro-latest"  # Change the AI model if needed (Check available models by running "models.py")
VOICE = "en-US-JennyNeural"  # Change this if you want a different voice (Available voices listed in "voice_list.txt")
USER_NAME = "YOUR_NAME_HERE"  # Your name here
OUTPUT_TEXT_FILE = f"response_{datetime.now().strftime('%Y%m%d-%H-%M-%S')}.txt"
OUTPUT_AUDIO_FILE = f"audio_{datetime.now().strftime('%Y%m%d-%H-%M-%S')}.mp3"

# Configure the API key for genai
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(AI_MODEL)


# Function to generate an AI response
def generate_response():
    question = input_text.get("1.0", tk.END).strip()
    if not question:
        messagebox.showwarning("Warning", "Please enter a question.")
        return

    # Generate the response using the AI model
    try:
        response = model.generate_content(question).candidates[0].content.parts[0].text
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, response)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while generating the response: {e}")

# Function to clear the input and output fields
def new_question():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Function to export the response to a .txt file
def export_text():
    response = output_text.get("1.0", tk.END).strip()
    if not response:
        messagebox.showwarning("Warning", "No response to export.")
        return

    with open(OUTPUT_TEXT_FILE, "w", encoding="utf-8") as file:
        file.write(response)
        messagebox.showinfo("Exported", f"Response exported as {OUTPUT_TEXT_FILE}")

# Asynchronous function to export the response to a .mp3 file
async def export_audio_async():
    response = output_text.get("1.0", tk.END).strip()
    if not response:
        messagebox.showwarning("Warning", "No response to export.")
        return

    try:
        communicate = edge_tts.Communicate(str(response).replace("#", "").replace("*", ""), VOICE)
        await communicate.save(OUTPUT_AUDIO_FILE)
        messagebox.showinfo("Exported", f"Audio exported as {OUTPUT_AUDIO_FILE}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while exporting the audio: {e}")

def export_audio():
    asyncio.run(export_audio_async())

# Configure the graphical interface with Tkinter
root = tk.Tk()
root.title("AI Interface")
root.geometry("1200x600")
root.configure(bg="#444444")

# Configure grid to center the elements
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Welcome title
welcome_label = tk.Label(root, text=f"Welcome, {USER_NAME}!", font=("Arial", 24), bg="#444444", fg="white")
welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

# Input text box
input_label = tk.Label(root, text="Input", font=("Arial", 16, "bold"), bg="#444444", fg="white")
input_label.grid(row=1, column=0, padx=10, sticky="w")
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
input_text.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

# Output text box
output_label = tk.Label(root, text="Output", font=("Arial", 16, "bold"), bg="#444444", fg="white")
output_label.grid(row=1, column=1, padx=10, sticky="w")
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
output_text.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

# Configure grid to expand text boxes
root.grid_rowconfigure(2, weight=1)

# Buttons
generate_response_button = tk.Button(root, text="Generate Response", font=("Arial", 14), bg="#007bff", fg="white", command=generate_response)
generate_response_button.grid(row=3, column=0, pady=20, sticky="n")

new_question_button = tk.Button(root, text="New Question", font=("Arial", 14), bg="#007bff", fg="white", command=new_question)
new_question_button.grid(row=3, column=1, sticky="w", padx=5)

export_text_button = tk.Button(root, text="Export Text", font=("Arial", 14), bg="#007bff", fg="white", command=export_text)
export_text_button.grid(row=3, column=1, padx=5)

export_audio_button = tk.Button(root, text="Export Audio", font=("Arial", 14), bg="#007bff", fg="white", command=export_audio)
export_audio_button.grid(row=3, column=1, sticky="e", padx=5)

root.mainloop()
