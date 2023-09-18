import tkinter as tk
import math
import re

def evaluate(event):
    try:
        expr = entry.get()

        replacements = {
           r'(\d+)sin': r'\1*math.sin(math.radians(',
           r'(\d+)cos': r'\1*math.cos(math.radians(',
           r'(\d+)tan': r'\1*math.tan(math.radians(',
           r'sin(\d+)': r'math.sin(math.radians(\1))',
           r'cos(\d+)': r'math.cos(math.radians(\1))',
           r'tan(\d+)': r'math.tan(math.radians(\1))',
           'log': 'math.log('
        }

        for key, val in replacements.items():
            expr = re.sub(key, val, expr)
        
        for val in replacements.values():
            count_open = expr.count(val)
            count_close = expr.count(')')
            if count_open > count_close:
                expr += ')' * (expr.count('(') - expr.count(')'))

        if "^2" in expr:
            result.set(float(expr.split("^2")[0]) ** 2)
        elif "√" in expr:
            result.set(math.sqrt(float(expr.split("√")[1])))
        elif "1/" in expr:
            result.set(1 / float(expr.split("1/")[1]))
        elif "!" in expr:
            result.set(math.factorial(int(expr.split("!")[0])))
        else:
            result.set(eval(expr))
    except Exception as e:
        result.set("Error")


def clear(event):
    entry.delete(0, tk.END)
    result.set("")

def change_color(color):
    app.configure(bg=color)
    button_frame.configure(bg=color)
    result_label.configure(bg=color)

app = tk.Tk()
app.title("Enhanced Calculator")

entry = tk.Entry(app, width=40)
entry.bind("<Return>", evaluate)

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '^2', '√', '1/', '!',
    'sin', 'cos', 'tan', 'log',
    'C', '0', '=', '+'
]

number_button_style = {
    "font": ("Arial", 16, "bold"),
    "bg": "#d3d3d3",
    "activebackground": "#a3a3a3",
    "borderwidth": 3,
    "relief": "ridge"
}

operator_button_style = {
    "font": ("Arial", 16, "bold"),
    "bg": "#f2a265",
    "activebackground": "#f28f53",
    "borderwidth": 3,
    "relief": "ridge"
}

function_button_style = {
    "font": ("Arial", 16, "bold"),
    "bg": "#f2d56d",
    "activebackground": "#f2bf60",
    "borderwidth": 3,
    "relief": "ridge"
}

row, col = 0, 0
for btn in buttons:
    button_command = (lambda b=btn: 
                      lambda: entry.insert(tk.END, b if b != "C" else ""))()
    style = {}
    if btn in ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']:
        style = number_button_style
    elif btn in ['/', '*', '-', '+', '=']:
        style = operator_button_style
    else:
        style = function_button_style

    tk.Button(button_frame, text=btn, width=5, height=2, command=button_command, **style).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

result = tk.StringVar()
result_label = tk.Label(app, textvariable=result, font=("Arial", 18))

colors = ["lightgray", "lightblue", "lightgreen", "lightyellow", "lightpink"]
selected_color = tk.StringVar()
selected_color.set(colors[0])
color_dropdown = tk.OptionMenu(app, selected_color, *colors, command=change_color)
color_dropdown.pack(pady=10)

entry.pack(pady=20)
result_label.pack(pady=20)

for button in button_frame.winfo_children():
    if button['text'] == 'C':
        button.bind('<Button-1>', clear)
    elif button['text'] == '=':
        button.bind('<Button-1>', evaluate)

app.mainloop()
