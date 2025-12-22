# 📐 Numerical Methods Project

This repository contains a collection of **Numerical Analysis methods** implemented in Python as part of a university project.  
The project provides **interactive GUIs** for each method and includes examples, iteration details, and results visualization.

---

## Project Overview

The project covers the following numerical methods:

1. **Newton–Raphson Method** – Root finding using derivative-based tangent line approximation.
2. **Secant Method** – Root finding without requiring derivatives.
3. **Jacobi Method** – Iterative solution for systems of linear equations.
4. **Linear Least Squares & Linearization** – Fits data to various models and selects the best using least squares.

Each method has its **own GUI**, **clear inputs and outputs**, and example usage to demonstrate functionality.

---

## 1️⃣ Newton–Raphson Method

> **Purpose:**  
> Find a root of a nonlinear equation using tangent-line approximation.  
> Ideal for functions where the derivative can be computed symbolically.

---

### 🔹 Mathematical Formula

\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]

---

### 🖥 GUI Preview

![Newton Method GUI](screenshots/newton.png)  
*Interactive GUI allows input of function, initial guess, tolerance, and max iterations.*

**Demo GIF:**  
![Newton Demo](screenshots/newton_demo.gif)

---

### ⚙️ Inputs

- **Function**: Enter as a string in SymPy format, e.g., `x**2 - 2`  
- **Initial guess \(x_0\)**: Starting point for iterations  
- **Tolerance**: Default `1e-6`  
- **Maximum iterations**: Default `100`  

---

### 📊 Outputs

- **Approximate root**  
- **Iteration table** with: Iteration number, x, f(x), Error  
- **Symbolic derivative** f'(x)  
- **Convergence message** (success or failure)

---

### 🧪 Example Usage

```python
from newton_method import newton_method

# Define the function as a string
func_str = "x**3 - 2*x - 5"

# Initial guess
x0 = 2

# Run Newton Method
result = newton_method(func_str, x0)

# Print the approximate root
print("Root:", result["root"])

Sample Output:  
Root: 2.094551  
Converged in 5 iterations
```

---

###⚠️ Notes

-The derivative is calculated automatically; no need to enter manually.

-If the derivative at a point is zero, the method fails.

-Always check convergence for difficult functions.

---

## 2️⃣ Secant Method

> **Purpose:**  
> Find a root of a nonlinear equation without requiring derivatives.  
> Useful when derivative calculation is difficult or expensive.

---

### 🔹 Mathematical Formula

\[
x_{n+1} = x_n - f(x_n)\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}
\]

---

### 🖥 GUI Preview

![Secant Method GUI](screenshots/secant.png)  
*Interactive GUI allows input of function, two initial guesses, tolerance, and max iterations.*

**Demo GIF:**  
![Secant Demo](screenshots/secant_demo.gif)

---

### ⚙️ Inputs

- **Function**: Enter as a string, e.g., `x**3 - 2*x - 5`  
- **Initial guesses \(x_0, x_1\)**: Two starting points  
- **Tolerance**: Default `1e-4`  
- **Maximum iterations**: Default `100`  

---

### 📊 Outputs

- **Approximate root**  
- **Iteration table** with: Iteration number, x0, x1, x2, f(x0), f(x1)  
- **Convergence message** (success or failure)

---

### 🧪 Example Usage

```python
from secant_method import secant_method

# Define the function
f = lambda x: x**3 - 2*x - 5

# Initial guesses
x0, x1 = 2, 3

# Run Secant Method
root, steps = secant_method(f, x0, x1)

print("Root:", root)
Sample Output:
Root: 2.094551
Converged in 6 iterations
```
###⚠️ Notes

This method does not require the derivative.

Convergence is not guaranteed; choose initial guesses carefully.

Division by zero can occur if f(x1) - f(x0) = 0.

