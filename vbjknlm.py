import tkinter as tk
import random

# ====== Настройки уровней сложности ======
levels = {
    "Легкий": (1, 50, 8),
    "Средний": (1, 100, 10),
    "Сложный": (1, 200, 12)
}

# ====== Игровые переменные ======
number = 0
attempts_left = 0
min_val = 1
max_val = 100
max_attempts = 10


def start_new_game():
    """Запуск новой игры с выбранным уровнем"""
    global number, attempts_left, min_val, max_val, max_attempts

    level = level_var.get()
    min_val, max_val, max_attempts = levels[level]
    number = random.randint(min_val, max_val)
    attempts_left = max_attempts

    result_label.config(text=f"Игра началась! Угадайте число от {min_val} до {max_val}")
    attempts_label.config(text=f"Осталось попыток: {attempts_left}")
    entry.delete(0, tk.END)
    check_button.config(state=tk.NORMAL)


def check_guess():
    """Проверка введённого числа"""
    global attempts_left

    if attempts_left <= 0:
        return

    try:
        guess = int(entry.get())
        attempts_left -= 1

        if guess < min_val or guess > max_val:
            result_label.config(text=f"Введите число от {min_val} до {max_val}")
            return

        if guess < number:
            result_label.config(text="Моё число больше.")
        elif guess > number:
            result_label.config(text="Моё число меньше.")
        else:
            result_label.config(text=f"🎉 Поздравляю! Вы угадали за {max_attempts - attempts_left} попыток!")
            check_button.config(state=tk.DISABLED)
            attempts_label.config(text="Вы победили!")
            return

        attempts_label.config(text=f"Осталось попыток: {attempts_left}")

        if attempts_left == 0 and guess != number:
            result_label.config(text=f"❌ Попытки закончились. Число было: {number}")
            check_button.config(state=tk.DISABLED)

    except ValueError:
        result_label.config(text="Введите корректное число!")


# ====== Интерфейс ======
window = tk.Tk()
window.title("Угадай число")
window.geometry("400x350")

# Заголовок
title_label = tk.Label(window, text="Угадай число", font=("Arial", 16))
title_label.pack(pady=10)

# Выбор уровня сложности
level_var = tk.StringVar(value="Средний")
level_frame = tk.Frame(window)
level_frame.pack(pady=5)

tk.Label(level_frame, text="Выберите уровень:").pack(side=tk.LEFT, padx=5)

for level in levels:
    tk.Radiobutton(level_frame, text=level, variable=level_var, value=level).pack(side=tk.LEFT)

# Кнопка новой игры
new_game_button = tk.Button(window, text="Новая игра", command=start_new_game, width=20)
new_game_button.pack(pady=5)

# Поле ввода
entry = tk.Entry(window, width=20, font=("Arial", 14))
entry.pack(pady=5)

# Кнопка проверки
check_button = tk.Button(window, text="Проверить", command=check_guess, width=20)
check_button.pack(pady=5)

# Результат
result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=5)

# Счётчик попыток
attempts_label = tk.Label(window, text="Осталось попыток: --", font=("Arial", 12), fg="gray")
attempts_label.pack(pady=5)

# Запуск окна
window.mainloop()