import tkinter as tk
from tkinter import scrolledtext
import random

responses = {
    'hello': ['Hi there!', "Hello! How can i help you?", "Hey! What's up ?"],
    'how are you': ["i'm doing great!", "feeling like a bot should __ awesome!", "All good thanks for asking!"],
    'your name': ['My name is PyBot ', "You can call me PyBot!", "I am PyBot, your assistant."],
    'bye': ["Goodbye", "See you later!", "Bye! Have a nice day!"]
}

def get_responce(user_msg):
    user_msg = user_msg.lower()
    for key in responses:
        if key in user_msg:
            return random.choice(responses[key])
    return "Sorry, I don't understand that"

def send_message():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return
    chat_window.insert(tk.END, "You: " + user_msg + "\n", "user")
    entry.delete(0, tk.END)
    bot_msg = get_responce(user_msg)
    chat_window.insert(tk.END, "Bot: " + bot_msg + "\n", "bot")

root = tk.Tk()
root.title("Pybot - ChatBot")
root.geometry("450x550")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=('Arial', 12))
chat_window.pack(pady=10)

chat_window.tag_config('user', foreground="blue")
chat_window.tag_config('bot', foreground="green")

entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.pack(pady=5, side=tk.LEFT, padx=5)

send_btn = tk.Button(root, text="Send", command=send_message, width=10, bg="lightblue")
send_btn.pack(pady=5, side=tk.LEFT)

root.mainloop()
