import tkinter as tk, random, string
def generate_password():
    length = int(length_entry.get())
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()
    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    if characters == '':
        password = 'Выберите хотя бы один вариант'
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")
app = tk.Tk()
app.title("Генератор пароля")
length_label = tk.Label(app, text="Длина пароля:")
length_label.pack()
length_entry = tk.Entry(app)
length_entry.pack()
upper_var = tk.BooleanVar()
upper_check = tk.Checkbutton(app, text="Включить заглавные буквы", variable=upper_var)
upper_check.pack()
lower_var = tk.BooleanVar()
lower_check = tk.Checkbutton(app, text="Включить строчные буквы", variable=lower_var)
lower_check.pack()
digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(app, text="Включить цифры", variable=digits_var)
digits_check.pack()
special_var = tk.BooleanVar()
special_check = tk.Checkbutton(app, text="Включить специальные символы", variable=special_var)
special_check.pack()
generate_button = tk.Button(app, text="Сгенерировать пароль", command=generate_password)
generate_button.pack()
password_label = tk.Label(app, text="Ваш пароль:")
password_label.pack()
password_entry = tk.Entry(app)
password_entry.pack()
app.mainloop()