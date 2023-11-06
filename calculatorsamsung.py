import tkinter as tk
from math import sqrt, factorial, sin, cos, tan, radians, log10, pi

def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Samsung Calculator")

entry = tk.Entry(root, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=20, ipady=20)

button_grid = [
    ['7', '8', '9', '/', 'sqrt'],
    ['4', '5', '6', '*', 'x^2'],
    ['1', '2', '3', '-', 'x^y'],
    ['0', '.', '=', '+', 'C'],
]

for i, row_buttons in enumerate(button_grid):
    for j, button in enumerate(row_buttons):
        if button == '=':
            tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=evaluate_expression).grid(row=i+1, column=j)
        elif button == 'C':
            tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda b=button: entry.delete(0, tk.END)).grid(row=i+1, column=j)
        else:
            tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda b=button: entry.insert(tk.END, b)).grid(row=i+1, column=j)

additional_buttons = [
    ('sin', 'cos', 'tan', 'log', 'pi'),
    ('(', ')', '!', '1/x', 'e'),
]

for i, row_buttons in enumerate(additional_buttons):
    for j, button in enumerate(row_buttons):
        if button == 'pi':
            tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda b=button: entry.insert(tk.END, str(pi))).grid(row=i+5, column=j)
        elif button == '1/x':
            tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda b=button: entry.insert(tk.END, "**(-1)")).grid(row=i+5, column=j)
        elif button == 'e':
            tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda b=button: entry.insert(tk.END, str(2.71828))).grid(row=i+5, column=j)
        else:
            tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda b=button: entry.insert(tk.END, b)).grid(row=i+5, column=j)

root.mainloop()