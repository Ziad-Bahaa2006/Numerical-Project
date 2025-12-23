import customtkinter as ctk
from tkinter import ttk
from newten_method import newton_method  
class NewtonMethodApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("light")
        self.title("Newton Method")
        self.geometry("950x680")
        self.resizable(False, False)

        # Title
        ctk.CTkLabel(
            self,
            text="Newton Method",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            self,
            text="Enter f(x) only – derivative is calculated automatically",
            text_color="gray",
            font=ctk.CTkFont(size=12, slant="italic")
        ).pack(pady=(0, 10))

        # Input Card
        input_card = ctk.CTkFrame(self, corner_radius=15)
        input_card.pack(padx=40, pady=10, fill="x")

        ctk.CTkLabel(input_card, text="f(x):", font=ctk.CTkFont(size=13)).grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.fx_entry = ctk.CTkEntry(input_card, width=400, height=40, corner_radius=10, font=ctk.CTkFont(size=13))
        self.fx_entry.grid(row=0, column=1, padx=20, pady=10)

        ctk.CTkLabel(
            input_card,
            text="Use Python/SymPy format: x**2, sqrt(x), sin(x), exp(x), log(x)",
            text_color="gray",
            font=ctk.CTkFont(size=11, slant="italic")
        ).grid(row=1, column=0, columnspan=2, pady=(0,10))

        ctk.CTkLabel(input_card, text="Initial Guess x₀:", font=ctk.CTkFont(size=13)).grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.x0_entry = ctk.CTkEntry(input_card, width=400, height=40, corner_radius=10, font=ctk.CTkFont(size=13))
        self.x0_entry.grid(row=2, column=1, padx=20, pady=10)

        # Buttons
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=15)

        self.run_btn = ctk.CTkButton(
            btn_frame,
            text="Run Newton Method",
            width=220,
            height=45,
            corner_radius=12,
            fg_color="#1abc9c",
            hover_color="#16a085",
            font=ctk.CTkFont(size=14, weight="bold"),
            cursor="hand2",
            command=self.run_method
        )
        self.run_btn.grid(row=0, column=0, padx=10)

        self.clear_btn = ctk.CTkButton(
            btn_frame,
            text="Clear",
            width=150,
            height=45,
            corner_radius=12,
            fg_color="#e67e22",
            hover_color="#d35400",
            font=ctk.CTkFont(size=13),
            cursor="hand2",
            command=self.clear_all
        )
        self.clear_btn.grid(row=0, column=1, padx=10)

        # Derivative
        self.derivative_label = ctk.CTkLabel(self, text="", text_color="gray", font=ctk.CTkFont(size=12))
        self.derivative_label.pack(pady=5)

        # Table / Iterations + Result
        table_result_frame = ctk.CTkFrame(self, corner_radius=15)
        table_result_frame.pack(padx=40, pady=10, fill="both", expand=True)

        # Result label ثابت فوق الجدول
        self.result_label = ctk.CTkLabel(
            table_result_frame,
            text="",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.result_label.pack(pady=(10,5))

        # Treeview
        tree_frame = ctk.CTkFrame(table_result_frame, corner_radius=10)
        tree_frame.pack(fill="both", expand=True, pady=(5,10))

        # Scrollbar
        self.tree_scroll = ctk.CTkScrollbar(tree_frame, orientation="vertical")
        self.tree_scroll.pack(side="right", fill="y")

        # Treeview
        self.tree = ttk.Treeview(
            tree_frame,
            columns=("Iter", "x", "f(x)", "Error"),
            show="headings",
            yscrollcommand=self.tree_scroll.set,
            height=12
        )
        self.tree.pack(fill="both", expand=True)
        self.tree_scroll.configure(command=self.tree.yview)

        # Columns setup
        self.tree.heading("Iter", text="Iter")
        self.tree.heading("x", text="x")
        self.tree.heading("f(x)", text="f(x)")
        self.tree.heading("Error", text="Error")

        self.tree.column("Iter", width=60, anchor="center")
        self.tree.column("x", width=200, anchor="center")
        self.tree.column("f(x)", width=200, anchor="center")
        self.tree.column("Error", width=200, anchor="center")
        
    # Run Method
    def run_method(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.result_label.configure(text="")
        self.derivative_label.configure(text="")

        func_str = self.fx_entry.get()
        x0 = self.x0_entry.get()

        try:
            x0_val = float(x0)
        except:
            self.result_label.configure(text="Invalid initial guess", text_color="red")
            return

        result = newton_method(func_str, x0_val)

        if result["error_msg"]:
            self.result_label.configure(text=result["error_msg"], text_color="red")
            return

        self.derivative_label.configure(text=f"f'(x) = {result['derivative']}")

        for it in result["iterations"]:
            i, x_val, fx_val, error = it
            self.tree.insert("", "end", values=(i, f"{x_val:.6f}", f"{fx_val:.6f}", f"{error:.6f}"))

        if result["converged"]:
            self.result_label.configure(text=f"Root ≈ {result['root']:.6f} (in {len(result['iterations'])} iterations)", text_color="green")
        else:
            self.result_label.configure(text="Method did not converge", text_color="red")

    def clear_all(self):
        self.fx_entry.delete(0, "end")
        self.x0_entry.delete(0, "end")
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.derivative_label.configure(text="")
        self.result_label.configure(text="")

if __name__ == "__main__":
    app = NewtonMethodApp()
    app.mainloop()
