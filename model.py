# Модуль для выполнения операций
import sympy


def execute_expr(expr: str) -> str:  # (5+3)*10 -> 80
    """Принимает на вход строку-пример.
    Возвращает результат примера."""
    try:
        result = str(sympy.simplify(expr))
    except ValueError:
        result = 'Неверный ввод'
    return result


def solve_eq(expr: str) -> str:  # x**3 - 8 = 0 -> "2"
    # x**2 - 1 = 0 -> "1,-1"
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    x = sympy.Symbol('x')
    try:
        temp = list(map(str, sympy.solve(expr, x)))
        result = ','.join(temp)
    except ValueError:
        result = 'Неверный ввод'
    return result


def simplify_pol(expr: str) -> str:  # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """"Упрощает введенный многочлен"""
    try:
        result = str(sympy.simplify(expr))
    except ValueError:
        result = 'Неверный ввод'
    return result
