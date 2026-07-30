import tkinter as tk
from tkinter import ttk, messagebox

from deep_translator import GoogleTranslator # type: ignore
import pyperclip # type: ignore

# -----------------------------
# Available Languages
# -----------------------------
languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Russian": "ru",
    "Arabic": "ar",
    "Italian": "it"
}


# -----------------------------
# Translate Function
# -----------------------------
def translate_text():

    text = input_box.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning(
            "Warning",
            "Please enter some text."
        )
        return

    source = languages[source_combo.get()]
    target = languages[target_combo.get()]

    try:

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror(
            "Translation Error",
            str(e)
        )


# -----------------------------
# Copy Function
# -----------------------------
def copy_text():

    translated = output_box.get("1.0", tk.END).strip()

    if translated:
        pyperclip.copy(translated)
        messagebox.showinfo(
            "Copied",
            "Translated text copied!"
        )


# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("Language Translator")
root.geometry("700x550")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# -----------------------------
# Source Language
# -----------------------------
frame1 = tk.Frame(root)
frame1.pack()

tk.Label(
    frame1,
    text="Source Language"
).grid(row=0, column=0, padx=10)

source_combo = ttk.Combobox(
    frame1,
    values=list(languages.keys()),
    width=20,
    state="readonly"
)
source_combo.current(0)
source_combo.grid(row=1, column=0)

# -----------------------------
# Target Language
# -----------------------------
tk.Label(
    frame1,
    text="Target Language"
).grid(row=0, column=1, padx=10)

target_combo = ttk.Combobox(
    frame1,
    values=list(languages.keys())[1:],
    width=20,
    state="readonly"
)
target_combo.current(0)
target_combo.grid(row=1, column=1)

# -----------------------------
# Input
# -----------------------------
tk.Label(
    root,
    text="Enter Text"
).pack(pady=(20, 5))

input_box = tk.Text(
    root,
    width=80,
    height=8
)
input_box.pack()

# -----------------------------
# Translate Button
# -----------------------------
translate_button = tk.Button(
    root,
    text="Translate",
    command=translate_text,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15
)

translate_button.pack(pady=15)

# -----------------------------
# Output
# -----------------------------
tk.Label(
    root,
    text="Translated Text"
).pack()

output_box = tk.Text(
    root,
    width=80,
    height=8
)
output_box.pack()

# -----------------------------
# Copy Button
# -----------------------------
copy_button = tk.Button(
    root,
    text="Copy Translation",
    command=copy_text,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold")
)

copy_button.pack(pady=15)

root.mainloop()
