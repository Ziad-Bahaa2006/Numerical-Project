import tkinter as tk
from tkinter import messagebox
import math

def secant_method(f, x0, x1, tol=1e-4, max_iter=100):
    steps = []
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        if f1 - f0 == 0:
            raise ValueError("Division by zero")
        x2 = x1 - f1*(x1 - x0)/(f1 - f0)
        steps.append((i+1, x0, x1, x2, f0, f1))
        if abs(x2 - x1) < tol:
            return x2, steps
        x0, x1 = x1, x2
    return x2, steps

def solve():
    try:
        func_text = func_entry.get()
        x0 = float(x0_entry.get())
        x1 = float(x1_entry.get())
        tol = float(tol_entry.get())
        f = lambda x: eval(func_text, {"x": x, "math": math})

        result, steps = secant_method(f, x0, x1, tol)
        result_label.config(text=f"Result: {result:.6f}")

        # عرض الخطوات
        steps_text.delete(1.0, tk.END)
        steps_text.insert(tk.END, f"{'Iter':<5}{'x0':<15}{'x1':<15}{'x2':<15}{'f(x0)':<15}{'f(x1)':<15}\n")
        steps_text.insert(tk.END, "-"*80 + "\n")
        for s in steps:
            steps_text.insert(tk.END, f"{s[0]:<5}{s[1]:<15.6f}{s[2]:<15.6f}{s[3]:<15.6f}{s[4]:<15.6f}{s[5]:<15.6f}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Secant Method")
root.configure(bg="#f0f8ff")  # خلفية زرقاء فاتحة

# خطوط كبيرة
font_label = ("Arial", 14, "bold")
font_entry = ("Arial", 14)
font_button = ("Arial", 14, "bold")
font_text = ("Courier", 12)

# مدخلات الدالة والقيم
tk.Label(root, text="f(x):", bg="#f0f8ff", font=font_label).grid(row=0, column=0, sticky="e", pady=5)
func_entry = tk.Entry(root, width=25, font=font_entry)
func_entry.insert(0, "x**2*math.exp(x)-1")
func_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="x0:", bg="#f0f8ff", font=font_label).grid(row=1, column=0, sticky="e", pady=5)
x0_entry = tk.Entry(root, font=font_entry)
x0_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="x1:", bg="#f0f8ff", font=font_label).grid(row=2, column=0, sticky="e", pady=5)
x1_entry = tk.Entry(root, font=font_entry)
x1_entry.grid(row=2, column=1, pady=5)

tk.Label(root, text="Tolerance:", bg="#f0f8ff", font=font_label).grid(row=3, column=0, sticky="e", pady=5)
tol_entry = tk.Entry(root, font=font_entry)
tol_entry.insert(0, "0.0001")
tol_entry.grid(row=3, column=1, pady=5)

solve_button = tk.Button(root, text="Solve", command=solve, bg="#4682b4", fg="white", font=font_button)
solve_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result:", bg="#f0f8ff", font=font_label)
result_label.grid(row=5, column=0, columnspan=2, pady=5)

# صندوق عرض الخطوات
steps_text = tk.Text(root, width=95, height=15, font=font_text, bg="#e6f2ff")
steps_text.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
