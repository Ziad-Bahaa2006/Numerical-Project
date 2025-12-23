# gui.py
# Numerical Computing Project GUI
# Uses Logic.py for computations

import tkinter as tk
from tkinter import messagebox, scrolledtext

from Logic import auto_fit_best_model


# =====================================
# Helper Functions
# =====================================

def parse_input(text):
    """
    Converts comma-separated input into a list of floats.
    """
    try:
        return [float(val.strip()) for val in text.split(",")]
    except ValueError:
        raise ValueError("Input must be comma-separated numbers.")


def format_model_result(model):
    """
    Formats model output for display.
    """
    lines = []
    lines.append(f"Model: {model['model']}")
    lines.append(f"a = {model['a']:.6f}")
    lines.append(f"b = {model['b']:.6f}")
    lines.append(f"Sum of squared residuals = {model['error']:.6f}")
    return "\n".join(lines)


# =====================================
# Main Solve Action
# =====================================

def solve():
    try:
        x = parse_input(entry_x.get())
        y = parse_input(entry_y.get())

        if len(x) != len(y):
            raise ValueError("x and y must have the same number of values.")

        result = auto_fit_best_model(x, y)

        output.delete(1.0, tk.END)

        output.insert(tk.END, "AUTOMATIC MODEL SELECTION\n")
        output.insert(tk.END, "-" * 40 + "\n\n")

        output.insert(tk.END, "All tested models:\n\n")

        for model in result["all_models"]:
            output.insert(tk.END, format_model_result(model))
            output.insert(tk.END, "\n" + "-" * 40 + "\n")

        output.insert(tk.END, "\nSELECTED BEST MODEL\n")
        output.insert(tk.END, "=" * 40 + "\n")
        output.insert(tk.END, format_model_result(result["best_model"]))

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =====================================
# GUI Layout
# =====================================

root = tk.Tk()
root.title("Numerical Computing – Least Squares & Linearization")

root.geometry("700x600")

# Input frame
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="x values (comma-separated):").grid(row=0, column=0, sticky="w")
entry_x = tk.Entry(frame_input, width=60)
entry_x.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="y values (comma-separated):").grid(row=1, column=0, sticky="w")
entry_y = tk.Entry(frame_input, width=60)
entry_y.grid(row=1, column=1, padx=5)

# Button
btn_solve = tk.Button(root, text="Auto Fit Best Model", command=solve)
btn_solve.pack(pady=10)

# Output area
output = scrolledtext.ScrolledText(root, width=80, height=25)
output.pack(padx=10, pady=10)

root.mainloop()
