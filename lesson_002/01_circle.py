#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()


# Также пусть есть координаты точки
point = (23, 34)
pi = 3.1415926
area_circle = pi * radius**2
print(round(area_circle, 4))
# Выведите на консоль True если точка point лежит внутри круга radius = 42, False - в противном случае
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
result_point1 = (point[0]**2+point[1]**2)**0.5
print(result_point1 < radius)
# Аналогично для другой точки
point_2 = (30, 30)
# Выведите на консоль True если точка point_2 лежит внутри круга radius = 42, False - в противном случае
result_point1 = (point_2[0]**2+point_2[1]**2)**0.5
print(result_point1 < radius)

# Формат результата выполнения (пример вывода на консоль)
#
# 7777.777
# False
# False


