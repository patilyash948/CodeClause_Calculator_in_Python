import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display the numbers and results
entry = tk.Entry(window, width=20, font=("Arial", 12))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for numbers and operators
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=10, command=button_equal).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(window, text=button, width=10, command=lambda num=button: button_click(num)).grid(row=row, column=col, padx=5, pady=5)

    col += 1

    if col > 3:
        col = 0
        row += 1

# Create a clear button
tk.Button(window, text="C", width=10, command=button_clear).grid(row=row, column=col, padx=5, pady=5)

# Start the main loop
window.mainloop()
