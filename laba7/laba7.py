# Предприятие может предоставить работу по одной специальности 4 женщинам, по другой - 6 мужчинам, по третьей - 3 работникам независимо от пола.
# Сформировать все возможные варианты заполнения вакантных мест, если имеются 14 претендентов: 6 женщин и 8 мужчин

# Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса.
#  Допускается использовать любую графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter.

import tkinter as tk
from tkinter import messagebox
import itertools
import timeit

def algorithm(women, men, total, s1, s2, s3):
    result = []
    for w in range(min(s1, women) + 1):
        for m in range(min(s2, men) + 1):
            for t in range(min(s3, total) + 1):
                if w <= women and m <= men and t <= (total - (w + m)):
                    if (w + m + t) <= total:
                        result.append((w, m, t))
    return result

def pythonF(women, men, total, s1, s2, s3):
    result = []
    for w in itertools.combinations(range(women), s1):
        for m in itertools.combinations(range(men), s2):
            for t in itertools.combinations(range(total), s3):
                if len(set(w).union(set(m))) <= women and len(set(t)) <= total:
                    if (len(w) + len(m) + len(t)) <= total:
                        result.append((w, m, t))
    return result

def calculate():
    try:
        women = int(entry_women.get())
        men = int(entry_men.get())
        total = women + men
        s1 = int(entry_s1.get())
        s2 = int(entry_s2.get())
        s3 = int(entry_s3.get())

        if women < 0 or men < 0 or s1 < 0 or s2 < 0 or s3 < 0:
            messagebox.showerror("ошибка", "значения не могут быть отрицательными!")
            return
        
        # алгоритм с циклами
        start_time_algo = timeit.default_timer()
        algo_result = algorithm(women, men, total, s1, s2, s3)
        end_time_algo = timeit.default_timer()

        # с itertools
        start_time_func = timeit.default_timer()
        python_result = pythonF(women, men, total, s1, s2, s3)
        end_time_func = timeit.default_timer()

      
        result_text.delete(1.0, tk.END)  
        result_text.insert(tk.END, f"результаты с циклом:\nколичество вариантов: {len(algo_result)}\nвремя: {end_time_algo - start_time_algo:.6f} секунд\n\n")
        result_text.insert(tk.END, f"результаты с itertools:\nколичество вариантов: {len(python_result)}\nвремя: {end_time_func - start_time_func:.6f} секунд\n")

    except ValueError:
        messagebox.showerror("ошибка", "введите корректные числовые значения!")


root = tk.Tk()
root.title("Алгоритм распределения работников по специальностям")

# поля ввода
label_women = tk.Label(root, text="Количество женщин:")
label_women.grid(row=0, column=0, padx=10, pady=5)

entry_women = tk.Entry(root)
entry_women.grid(row=0, column=1, padx=10, pady=5)

label_men = tk.Label(root, text="Количество мужчин:")
label_men.grid(row=1, column=0, padx=10, pady=5)

entry_men = tk.Entry(root)
entry_men.grid(row=1, column=1, padx=10, pady=5)

label_s1 = tk.Label(root, text="Требуется женщин для специальности 1:")
label_s1.grid(row=2, column=0, padx=10, pady=5)

entry_s1 = tk.Entry(root)
entry_s1.grid(row=2, column=1, padx=10, pady=5)

label_s2 = tk.Label(root, text="Требуется мужчин для специальности 2:")
label_s2.grid(row=3, column=0, padx=10, pady=5)

entry_s2 = tk.Entry(root)
entry_s2.grid(row=3, column=1, padx=10, pady=5)

label_s3 = tk.Label(root, text="Требуется работников для специальности 3:")
label_s3.grid(row=4, column=0, padx=10, pady=5)

entry_s3 = tk.Entry(root)
entry_s3.grid(row=4, column=1, padx=10, pady=5)

calc_button = tk.Button(root, text="Рассчитать", command=calculate)
calc_button.grid(row=5, column=0, columnspan=2, pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()

