# pylint: skip-file

"""
Вычислить среднюю скорость.
Ввести данные с клавиатуры и преобразовать тип str к float
"""

s = input("Enter distance, S = ")
v = input("Enter time. T = ")
print(s)
print(v)
avg_speed = float(s) / float(v)
print(f"Avg speed is {round(avg_speed, 1)}")
