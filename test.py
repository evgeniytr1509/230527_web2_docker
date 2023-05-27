import tkinter as tk

def on_button_click():
    label.config(text="Привет, мир!")

# Создаем главное окно
window = tk.Tk()
window.title("Пример программы с Tkinter")

# Создаем метку (label)
label = tk.Label(window, text="Нажмите кнопку")
label.pack(pady=10)

# Создаем кнопку
button = tk.Button(window, text="Нажми меня", command=on_button_click)
button.pack()

# Запускаем главный цикл обработки событий
window.mainloop()