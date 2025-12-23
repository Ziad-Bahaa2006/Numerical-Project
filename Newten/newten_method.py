import sympy as sp

def newton_method(func_str, x0, tol=1e-6, max_iter=100):
    """
    Newton Method لحساب جذر الدالة

    Parameters:
        func_str (str): الدالة كنص (Python/SymPy format)
        x0 (float): التخمين الابتدائي
        tol (float): التوليرانس
        max_iter (int): أقصى عدد Iterations

    Returns:
        result (dict): يحتوي على:
            'iterations': قائمة tuples (i, x, f(x), error)
            'root': الجذر لو وجد أو None
            'converged': True/False
            'derivative': f'(x)
            'error_msg': رسالة خطأ لو فشلت
    """
    result = {
        "iterations": [],
        "root": None,
        "converged": False,
        "derivative": None,
        "error_msg": None
    }

    try:
        x = sp.symbols('x')
        fx = sp.sympify(func_str)
        dfx = sp.diff(fx, x)
        result["derivative"] = dfx
        x_val = float(x0)
    except Exception as e:
        result["error_msg"] = f"Invalid input: {e}"
        return result

    for i in range(1, max_iter + 1):
        fx_val = float(fx.subs(x, x_val))
        dfx_val = float(dfx.subs(x, x_val))

        if dfx_val == 0:
            result["error_msg"] = "Derivative is zero – method failed"
            return result

        x_new = x_val - fx_val / dfx_val #newten formula
        error = abs(x_new - x_val)

        result["iterations"].append((i, x_val, fx_val, error))

        if error < tol:
            result["root"] = x_new
            result["converged"] = True
            return result

        x_val = x_new

    result["error_msg"] = "Method did not converge"
    return result
