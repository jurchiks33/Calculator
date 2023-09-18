import tkinter as tk

def evaluate(event):
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

def clear(event):
    entry.delete(0, tk.END)
    result.set("")

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
for button in buttons:
    tk.Button(button_frame, text=button, width=5, height=2, command=lambda b=button: entry.insert(tk.END, b if b != "C" else "")).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

result = tk.StringVar()
result_label = tk.Label(app, textvariable=result, font=("Arial", 18))

entry.pack(pady=20)
result_label.pack(pady=20)

clear_button = button_frame.winfo_children()[12]
clear_button.bind('<Button-1>', clear)

equal_button = button_frame.winfo_children()[14]
equal_button.bind('<Button-1>', evaluate)

app.mainloop()
