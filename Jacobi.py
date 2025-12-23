import tkinter as tk
from tkinter import messagebox
import numpy as np

def jacobi_method(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()

    for _ in range(max_iter):
        x_new = np.zeros(n)

        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            if A[i][i] == 0:
                return None
            x_new[i] = (b[i] - s) / A[i][i]

        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new

        x = x_new

    return None


def solve():
    try:
        n = int(entry_n.get())

        A = []
        for i in range(n):
            row = list(map(float, A_entries[i].get().split()))
            if len(row) != n:
                raise ValueError
            A.append(row)

        b = list(map(float, entry_b.get().split()))
        x0 = list(map(float, entry_x0.get().split()))

        tol = float(entry_tol.get())
        max_iter = int(entry_iter.get())

        if len(b) != n or len(x0) != n:
            raise ValueError

        A = np.array(A)
        b = np.array(b)
        x0 = np.array(x0)

        result = jacobi_method(A, b, x0, tol, max_iter)

        if result is None:
            messagebox.showerror("Error", "Method did not converge or invalid matrix.")
        else:
            output.set("Solution:\n" + "\n".join(f"x{i+1} = {result[i]:.6f}" for i in range(n)))

    except:
        messagebox.showerror("Input Error", "Please check your inputs.")


# ================= GUI =================

root = tk.Tk()
root.title("Jacobi Method Solver")

tk.Label(root, text="Number of equations (n):").grid(row=0, column=0)
entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1)

tk.Label(root, text="Matrix A (each row space-separated):").grid(row=1, column=0, columnspan=2)

A_entries = []
for i in range(5):  # max 5x5 for simplicity
    e = tk.Entry(root, width=40)
    e.grid(row=2+i, column=0, columnspan=2)
    A_entries.append(e)

tk.Label(root, text="Vector b:").grid(row=7, column=0)
entry_b = tk.Entry(root, width=40)
entry_b.grid(row=7, column=1)

tk.Label(root, text="Initial guess x0:").grid(row=8, column=0)
entry_x0 = tk.Entry(root, width=40)
entry_x0.grid(row=8, column=1)

tk.Label(root, text="Tolerance:").grid(row=9, column=0)
entry_tol = tk.Entry(root)
entry_tol.grid(row=9, column=1)

tk.Label(root, text="Max iterations:").grid(row=10, column=0)
entry_iter = tk.Entry(root)
entry_iter.grid(row=10, column=1)

tk.Button(root, text="Solve", command=solve).grid(row=11, column=0, columnspan=2)

output = tk.StringVar()
tk.Label(root, textvariable=output, fg="blue").grid(row=12, column=0, columnspan=2)

root.mainloop()
