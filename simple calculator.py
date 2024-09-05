import tkinter as tk
def evaluate():
    try:
        result = eval(entry.get())
        result_var.set(result)
    except Exception as e:
        result_var.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

result_var = tk.StringVar()

entry = tk.Entry(root, width=20, font=('Verdana', 16), bd=3, insertwidth=4,  justify='left',bg='black',fg='white')
entry.grid(row=0, column=0, columnspan=4)

result_label = tk.Label(root, textvariable=result_var, font=('Verdana', 16), bg='grey', bd=5, anchor='e')
result_label.grid(row=1, column=0, columnspan=4, sticky='nsew')

def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 2
col = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16), command=evaluate)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16),
                        command=lambda b=button: button_click(b))
    btn.grid(row=row, column=col, sticky='nsew')
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(4):
    root.grid_rowconfigure(i + 2, weight=1)

root.mainloop()
