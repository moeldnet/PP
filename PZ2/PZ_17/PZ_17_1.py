# Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).

import tkinter as tk
from tkinter import ttk, filedialog

def submit_form():
    """Функция для обработки отправки формы."""
    print("Форма отправлена!")
    print(f"Имя: {name_entry.get()}")
    print(f"Email: {email_entry.get()}")
    print(f"Телефон: {phone_entry.get()}")
    print(f"Тема: {subject_combobox.get()}")
    print(f"Сообщение: {message_text.get('1.0', tk.END)}")
    print(f"Файлы: {file_path}")

def attach_file():
    """Функция для прикрепления файлов."""
    global file_path
    file_path = filedialog.askopenfilename()
    file_label.config(text=file_path.split('/')[-1] if file_path else "No file chosen")

# Создание основного окна
root = tk.Tk()
root.title("Contact Form")
root.geometry("500x600")

# Переменные
file_path = ""

# Стиль для обязательных полей
style = ttk.Style()
style.configure("Required.TLabel", foreground="red")

# Заголовок формы
title_label = ttk.Label(root, text="Contact Form", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Поле "Имя"
name_frame = ttk.Frame(root)
name_frame.pack(pady=5, padx=10, fill=tk.X)

name_label = ttk.Label(name_frame, text="Name *", style="Required.TLabel")
name_label.pack(anchor=tk.W)

name_entry = ttk.Entry(name_frame)
name_entry.pack(fill=tk.X)
name_hint = ttk.Label(name_frame, text="First & Last Name", foreground="gray")
name_hint.pack(anchor=tk.W)

# Поле "Email"
email_frame = ttk.Frame(root)
email_frame.pack(pady=5, padx=10, fill=tk.X)

email_label = ttk.Label(email_frame, text="Email *", style="Required.TLabel")
email_label.pack(anchor=tk.W)

email_entry = ttk.Entry(email_frame)
email_entry.pack(fill=tk.X)
email_hint = ttk.Label(email_frame, text="Email", foreground="gray")
email_hint.pack(anchor=tk.W)

# Поле "Телефон"
phone_frame = ttk.Frame(root)
phone_frame.pack(pady=5, padx=10, fill=tk.X)

phone_label = ttk.Label(phone_frame, text="Phone Number *", style="Required.TLabel")
phone_label.pack(anchor=tk.W)

phone_entry = ttk.Entry(phone_frame)
phone_entry.pack(fill=tk.X)
phone_hint = ttk.Label(phone_frame, text="Phone Number", foreground="gray")
phone_hint.pack(anchor=tk.W)

# Поле "Тема"
subject_frame = ttk.Frame(root)
subject_frame.pack(pady=5, padx=10, fill=tk.X)

subject_label = ttk.Label(subject_frame, text="Subject *", style="Required.TLabel")
subject_label.pack(anchor=tk.W)

subject_combobox = ttk.Combobox(subject_frame, values=["Select Subject", "Support", "Feedback", "Other"])
subject_combobox.current(0)
subject_combobox.pack(fill=tk.X)

# Поле "Сообщение"
message_frame = ttk.Frame(root)
message_frame.pack(pady=5, padx=10, fill=tk.X)

message_label = ttk.Label(message_frame, text="Leave us a few words *", style="Required.TLabel")
message_label.pack(anchor=tk.W)

message_text = tk.Text(message_frame, height=5)
message_text.pack(fill=tk.X)

# Поле "Прикрепление файлов"
file_frame = ttk.Frame(root)
file_frame.pack(pady=5, padx=10, fill=tk.X)

file_label_main = ttk.Label(file_frame, text="File Attachments")
file_label_main.pack(anchor=tk.W)

attach_button = ttk.Button(file_frame, text="Choose Files", command=attach_file)
attach_button.pack(anchor=tk.W)

file_label = ttk.Label(file_frame, text="No file chosen", foreground="gray")
file_label.pack(anchor=tk.W)

# Капча
captcha_frame = ttk.Frame(root)
captcha_frame.pack(pady=10, padx=10, fill=tk.X)

captcha_label = ttk.Label(captcha_frame, text="I'm not a robot")
captcha_label.pack(anchor=tk.W)

captcha_hint = ttk.Label(captcha_frame, text="reCAPTCHA Privacy Terms", foreground="gray")
captcha_hint.pack(anchor=tk.W)

# Кнопка "Отправить"
submit_button = ttk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=10)

root.mainloop()