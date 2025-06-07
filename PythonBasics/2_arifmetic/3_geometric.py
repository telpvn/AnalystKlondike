# pylint: skip-file

"""
Проверить, являютя ли три числа последовательными членами геометрической прогрессии.
"""

a = 2
b = 4
c = 9

mult = b / a
expected_mult = c / b
if mult == expected_mult:
    print("geometric progression")
else:
    print("No progression")