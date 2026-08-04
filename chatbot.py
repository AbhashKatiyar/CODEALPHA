import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.metrics.pairwise import cosine_similarity # type: ignore

from faqs import FAQS

# Loading the FAQs from faqs.py

questions = [faq["question"] for faq in FAQS]
answers = [faq["answer"] for faq in FAQS]

# NLP Model for Processing the Questions and Answers

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

question_vectors = vectorizer.fit_transform(questions)

# Chatbot Logic

def chatbot_response(user_question):

    user_question = user_question.strip()

    if user_question == " ":
        return "Please enter a question."

    user_vector = vectorizer.transform([user_question])

    similarity = cosine_similarity(user_vector, question_vectors)

    best_index = similarity.argmax()

    confidence = similarity[0][best_index]

    if confidence < 0.20:
        return ("Sorry, I couldn't find an answer to the question you asked.\nTry asking a Python-related question.")

    return answers[best_index]


# Utility Functions such as Date and Time, Adding Messages to the Chat Area

def current_time():
    return datetime.now().strftime("%H:%M")


def add_message(sender, message):

    chat.configure(state="normal")

    if sender == "You":
        chat.insert(tk.END, f"\nYou [{current_time()}]\n", "user")

        chat.insert(tk.END, message + "\n", "user_msg")

    else:
        chat.insert(tk.END, f"\nPython Chatbot [{current_time()}]\n", "bot")

        chat.insert(tk.END, message + "\n", "bot_msg")

    chat.configure(state="disabled")

    chat.see(tk.END)


# Send Button Interface

def send():

    question = entry.get().strip()

    if question == "":
        return

    add_message("You", question)

    answer = chatbot_response(question)

    add_message("Bot", answer)

    entry.delete(0, tk.END)


# Enter Key also Sends the Message

def enter_pressed(event):
    send()

# Main Window User Interface

window = tk.Tk()

window.title("Python FAQ Chatbot")

window.geometry("850x650")

window.configure(bg="#ECEFF1")

# Header

header = tk.Label(
    window,
    text="🐍 Python FAQ Chatbot",
    bg="#1565C0",
    fg="#f9ef2a",
    font=("Helvetica", 25, "bold"),
    pady=15
)

header.pack(fill="x")

# Chat Area

chat = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    font=("Calibri", 12),
    bg="white",
    fg="black",
    padx=10,
    pady=10,
    state="disabled"
)

chat.pack(
    padx=15,
    pady=15,
    fill="both",
    expand=True
)

# Message Styles

chat.tag_config(
    "user",
    foreground="#00FF00",
    font=("Helvetica", 11, "bold")
)

chat.tag_config(
    "bot",
    foreground="#003CFF",
    font=("Helvetica", 11, "bold")
)

chat.tag_config(
    "user_msg",
    foreground="#00FF00",
    background="#FFFFFF",
    lmargin1=20,
    lmargin2=20,
    spacing3=8
)

chat.tag_config(
    "bot_msg",
    foreground="#0022FF",
    background="#FFFFFF",
    lmargin1=20,
    lmargin2=20,
    spacing3=8
)

# Welcome Message

chat.configure(state="normal")

chat.insert(
    tk.END,
    "Python Bot\n",
    "bot"
)

chat.insert(
    tk.END,
    "Hello Abhash! 👋\n"
    "I'm your Python FAQ Chatbot.\n\n"
    "You can ask me questions related to Python programming, and I'll do my best to provide you with accurate answers.\n\n",
    "bot_msg"
)

chat.configure(state="disabled")

# Bottom Frame

bottom = tk.Frame(
    window,
    bg="#ECEFF1"
)

bottom.pack(
    fill="x",
    padx=15,
    pady=10
)

# Entry

entry = tk.Entry(
    bottom,
    font=("Calibri", 13),
    width=60,
    relief="solid",
    bd=1
)

entry.pack(
    side="left",
    padx=(0, 10),
    ipady=8,
    fill="x",
    expand=True
)

entry.bind("<Return>", enter_pressed)

# Send Button

send_button = tk.Button(
    bottom,
    text="Send",
    command=send,
    bg="#000FFF",
    fg="white",
    font=("Helvetica", 15, "bold"),
    width=10,
    cursor="hand2"
)

send_button.pack(side="left", padx=5)

# Exit Button

exit_button = tk.Button(
    bottom,
    text="Exit",
    command=window.destroy,
    bg="#FF0000",
    fg="white",
    font=("Helvetica", 15, "bold"),
    width=10,
    cursor="hand2"
)

exit_button.pack(side="left")

entry.focus()

window.mainloop()
