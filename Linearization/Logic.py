# Logic.py
# Numerical Computing Project
# Linear Least Squares Regression & Linearization
# Based strictly on lecture PDF formulas

from math import log, exp
from typing import List, Dict


# ==================================================
# Core Least Squares Utilities
# ==================================================

def compute_summations(X: List[float], Y: List[float]) -> Dict:
    n = len(X)
    return {
        "n": n,
        "sum_x": sum(X),
        "sum_y": sum(Y),
        "sum_x2": sum(x ** 2 for x in X),
        "sum_xy": sum(x * y for x, y in zip(X, Y))
    }


def solve_normal_equations(sums: Dict) -> Dict:
    n = sums["n"]
    Sx = sums["sum_x"]
    Sy = sums["sum_y"]
    Sx2 = sums["sum_x2"]
    Sxy = sums["sum_xy"]

    denominator = n * Sx2 - Sx ** 2
    if denominator == 0:
        raise ValueError("Normal equations are singular.")

    a = (n * Sxy - Sx * Sy) / denominator
    b = (Sy * Sx2 - Sx * Sxy) / denominator

    return {"a": a, "b": b}


# ==================================================
# Model Fitting (Lecture-Based)
# ==================================================

def fit_linear(x: List[float], y: List[float]) -> Dict:
    sums = compute_summations(x, y)
    coeffs = solve_normal_equations(sums)

    return {
        "model": "Linear: y = ax + b",
        "a": coeffs["a"],
        "b": coeffs["b"],
        "sums": sums
    }


def fit_exponential(x: List[float], y: List[float]) -> Dict:
    # y = b e^(ax)  → ln(y) = ax + ln(b)
    Y = [log(val) for val in y]
    sums = compute_summations(x, Y)
    coeffs = solve_normal_equations(sums)

    return {
        "model": "Exponential: y = b e^(ax)",
        "a": coeffs["a"],
        "b": exp(coeffs["b"]),
        "sums": sums
    }


def fit_power(x: List[float], y: List[float]) -> Dict:
    # y = b x^a → ln(y) = a ln(x) + ln(b)
    X = [log(val) for val in x]
    Y = [log(val) for val in y]
    sums = compute_summations(X, Y)
    coeffs = solve_normal_equations(sums)

    return {
        "model": "Power: y = b x^a",
        "a": coeffs["a"],
        "b": exp(coeffs["b"]),
        "sums": sums
    }


def fit_growth_rate(x: List[float], y: List[float]) -> Dict:
    # y = ax / (b + x)
    # 1/y = (b/a)(1/x) + (1/a)
    X = [1 / val for val in x]
    Y = [1 / val for val in y]
    sums = compute_summations(X, Y)
    coeffs = solve_normal_equations(sums)

    A = coeffs["a"]
    B = coeffs["b"]

    a = 1 / B
    b = A * a

    return {
        "model": "Growth Rate: y = ax / (b + x)",
        "a": a,
        "b": b,
        "sums": sums
    }


# ==================================================
# Prediction Functions
# ==================================================

def predict_linear(x, a, b):
    return [a * xi + b for xi in x]


def predict_exponential(x, a, b):
    return [b * exp(a * xi) for xi in x]


def predict_power(x, a, b):
    return [b * (xi ** a) for xi in x]


def predict_growth_rate(x, a, b):
    return [(a * xi) / (b + xi) for xi in x]


# ==================================================
# Error Metric
# ==================================================

def compute_residual_error(y_true, y_pred):
    return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred))


# ==================================================
# Automatic Model Selection
# ==================================================

def auto_fit_best_model(x: List[float], y: List[float]) -> Dict:
    results = []

    # Linear
    linear = fit_linear(x, y)
    y_hat = predict_linear(x, linear["a"], linear["b"])
    linear["error"] = compute_residual_error(y, y_hat)
    results.append(linear)

    # Exponential (y > 0)
    if all(val > 0 for val in y):
        exp_model = fit_exponential(x, y)
        y_hat = predict_exponential(x, exp_model["a"], exp_model["b"])
        exp_model["error"] = compute_residual_error(y, y_hat)
        results.append(exp_model)

    # Power (x > 0 and y > 0)
    if all(val > 0 for val in x) and all(val > 0 for val in y):
        power = fit_power(x, y)
        y_hat = predict_power(x, power["a"], power["b"])
        power["error"] = compute_residual_error(y, y_hat)
        results.append(power)

    # Growth Rate (x ≠ 0, y ≠ 0)
    if all(val != 0 for val in x) and all(val != 0 for val in y):
        growth = fit_growth_rate(x, y)
        y_hat = predict_growth_rate(x, growth["a"], growth["b"])
        growth["error"] = compute_residual_error(y, y_hat)
        results.append(growth)

    best_model = min(results, key=lambda m: m["error"])

    return {
        "best_model": best_model,
        "all_models": results
    }
