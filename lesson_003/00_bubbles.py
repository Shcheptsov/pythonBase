# -*- coding: utf-8 -*-

import simple_draw as sd
import math
sd.resolution = (1200, 600)


# point = sd.get_point(100, 100)
# radius = 50


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# for _ in range(3):
#     sd.circle(center_position=point, radius=radius, width=1)
#     radius += 5

# Написать функцию рисования пузырька, принммающую 2 параметра: точка рисовании и шаг
# def print_bubble(point_print, step):
#     radius = 50
#     for _ in range(3):
#         sd.circle(center_position=point_print, radius=radius, width=1)
#         radius += step
#
#
# print_bubble(point_print=point, step=5)

# Нарисовать 10 пузырьков в ряд
# def print_bubble():
#     x = 100
#     radius = 50
#     for _ in range(10):
#         point = sd.get_point(x=x, y=100)
#         sd.circle(center_position=point, radius=radius, width=1)
#         x += 100
#
#
# print_bubble()

# Нарисовать три ряда по 10 пузырьков
# def print_bubble():
#     y = 100
#     radius = 50
#     for _ in range(3):
#         x = 100
#         for _ in range(10):
#             point = sd.get_point(x=x, y=y)
#             sd.circle(center_position=point, radius=radius, width=1)
#             x += 100
#         y += 100
#
#
# print_bubble()

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
def rand_bubble():
    radius = 100
    for _ in range(100):
        point = sd.random_point()
        sd.circle(center_position=point, radius=radius, width=1)


rand_bubble()

sd.pause()
