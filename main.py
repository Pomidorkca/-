from tkinter import *
import random
import json
b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
a = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
c = ["_", "*", "$", "%"]
password = ""
window = Tk()
window.title("Random Password Generator")
Label(window, text="Выберите настройки для пароля:", font=("Arial", 12)).pack(pady=10)
#--------------------------Чебоксы------------------------------------------
def check_settings():
    digits = use_digits.get()
    letters = use_letters.get()
    specials = use_specials.get()
use_digits = BooleanVar()
use_letters = BooleanVar()
use_specials = BooleanVar()
Checkbutton(window, text="Использовать цифры", variable=use_digits, font=("Arial", 12)).pack(anchor=W, padx=50)
Checkbutton(window, text="Использовать буквы", variable=use_letters, font=("Arial", 12)).pack(anchor=W, padx=50)
Checkbutton(window, text="Использовать спецсимволы", variable=use_specials, font=("Arial", 12)).pack(anchor=W, padx=50)
Label(window, text="------------------------------------------------------------------------------------").pack(pady=10)
use_digits.set(True)
#------------------------Курсор------------------------------------------------
length_slider = Scale(window,
    from_=4,               # Минимальная длина пароля
    to=32,                 # Максимальная длина пароля
    orient=HORIZONTAL,  # Горизонтальный вид
    label="Длина пароля  ", font=("Arial", 11))
length_slider.pack(padx=50)
length_slider.set(12)
Label(window, text="------------------------------------------------------------------------------------").pack(pady=10)
#-----------------------Генерация----------------------------------------------
def create_random_password():
    global password
    current_length = length_slider.get()
    available_chars = []
    if use_digits.get():
        available_chars += a
    if use_letters.get():
        available_chars += b
    if use_specials.get():
        available_chars += c
    if len(available_chars) == 0:
        result_label.config(text="Выберите хотя бы один тип символов!")
        return
    password_list = random.choices(available_chars, k=current_length)
    password = "".join(password_list)
    result_label.config(text=f"Готовый пароль: {password}")
    gen_btn.config(bg="green", text="Сгенерировано")
gen_btn = Button(window, text="Сгенерировать", command=create_random_password, bg="red", fg="white", font=("Arial", 12))
gen_btn.pack(pady=5)
result_label = Label(window, text="Ожидаем конца настроек", font=("Arial", 12))
result_label.pack(pady=10)
Label(window, text="------------------------------------------------------------------------------------").pack(pady=10)
#------------------------JSON-------------------------------------
def load_data():
    try:
        with open('passwords.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return []
def save_data():
    if password == "":
        history_label.config(text="Сначала сгенерируйте пароль!")
        return
    data = load_data()
    data.append(password)
    with open('passwords.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    history_label.config(text="Текущий пароль сохранен!")
def clear_data():
    with open('passwords.json', 'w', encoding='utf-8') as file:
        json.dump([], file, ensure_ascii=False, indent=4)
    history_label.config(text="История очищена!")
def see_data():
    data = load_data()
    if len(data) == 0:
        history_label.config(text="История пуста")
    else:
        formatted_history = "\n".join(str(item) for item in data)
        history_label.config(text=f"Ваша история:\n{formatted_history}")
Label(window, text="Настройки истории:", font=("Arial", 12)).pack(padx=50)
Button(window, text="Сохранить этот пароль в историю", command=save_data).pack(anchor=W, padx=50, pady=2)
Button(window, text="Очистить историю", command=clear_data).pack(anchor=W, padx=50, pady=2)
Button(window, text="Посмотреть историю", command=see_data).pack(anchor=W, padx=50, pady=2)
Label(window, text="------------------------------------------------------------------------------------").pack(pady=10)
history_label = Label(window, text="Здесь будет история", font=("Arial", 12))
history_label.pack(padx=50, pady=10)
window.mainloop()