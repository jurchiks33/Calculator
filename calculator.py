import tkinter as tk

def on_calculate():
    try:
        result = eval(entry.get())
        label.config(text=f"Result: {result}")
    except Exception as e:
        label.config(text=f"Error: {str(e)}")

app = tk.Tk()
app.title("Basic Calculator")

entry = tk.Entry(app, width=40)
entry.pack(pady=20)

calculate_button = tk.Button(app, text="Calculate", command=on_calculate)
calculate_button.pack(pady=10)

label = tk.Label(app, text="Result: ")
label.pack(pady=20)

app.mainloop()