
"""
Project Name: GUI Simple Calculator
Author: Sunil 
Date: 6 Feb 2026
Description: A simple GUI calculator built using Python and Tkinter.
"""

# your code starts from here


import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry box
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="x", padx=10, pady=10)

# Function to insert value
def press(value):
    entry.insert(tk.END, value)

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button frame
frame = tk.Frame(root)
frame.pack()

# Buttons list
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons
row = 0
col = 0
for button in buttons:
    if button == '=':
        tk.Button(frame, text=button, width=5, height=2,
                  font=("Arial", 14), command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(frame, text=button, width=5, height=2,
                  font=("Arial", 14),
                  command=lambda b=button: press(b)).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="Clear", width=20, height=2,
          font=("Arial", 14), command=clear).pack(pady=10)

# Run app
root.mainloop()
