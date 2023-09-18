import tkinter as tk

def evaluate(event):
    try:
        result.set(eval(entry.get()))
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
    'C', '0', '=', '+'
]

row, col = 0, 0
for btn in buttons:
    button_command = lambda b=btn: entry.insert(tk.END, b if b != "C" else "")
    tk.Button(button_frame, text=btn, width=5, height=2, command=button_command).grid(row=row, column=col)
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

clear_button = button_frame.winfo_children()[12]
clear_button.bind('<Button-1>', clear)

equal_button = button_frame.winfo_children()[14]
equal_button.bind('<Button-1>', evaluate)

app.mainloop()
