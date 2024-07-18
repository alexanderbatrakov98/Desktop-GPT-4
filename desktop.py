from g4f.client import Client

client = Client()

import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import tkinter as tk
from tkinter import messagebox

class MessageSenderApp:
    def __init__(self, master):
        self.master = master
        master.title('GPT-4o')
        self.text_input = tk.Entry(master, width=50, bg='white')
        self.text_input.pack(pady=20)

        self.send_button = tk.Button(master, text="Отправить", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        message = self.text_input.get()
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": {message}}],
        )
        if message:
            messagebox.showinfo("ChatGPT", f"Ответ: {response.choices[0].message.content}")
        else:
            messagebox.showerror("Ошибка", "Пожалуйста введите сообщение!")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")
    root.resizable(False, False)
    app = MessageSenderApp(root)
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()
    canvas.create_text(100, 20, text="Автор кода:Batrakov", font=("Arial", 10), fill="black")
    canvas.create_text(100, 40, text="github.com/alexanderbatrakov98", font=("Arial", 10), fill="black")
    root.mainloop()
