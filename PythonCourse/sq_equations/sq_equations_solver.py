from math import sqrt


def _calculate_d(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c


def solve_equation(a: float, b: float, c: float) -> (float, float):
    d = _calculate_d(a, b, c)
    if d > 0:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x, None
    else:
        return None, None


def print_equation(a: float, b: float, c: float):
    x1, x2 = solve_equation(a, b, c)
    print(f"Equation {a} * x ^ 2 + {b} * x + {c} = 0")
    if x1 is not None and x2 is not None:
        print(f'Two roots: x1 = {x1}, x2 = {x2}')
    elif x1 is not None and x2 is not None:
        print(f'One roots: x = {x1}')
    else:
        print('No roots')


print_equation(4, 3, -1)
