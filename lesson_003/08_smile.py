# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random as rand
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def draw_smile(current_x, current_y, color=sd.COLOR_DARK_PURPLE):
    bot_l = sd.get_point(current_x, current_y)
    top_r = sd.get_point(current_x + 150, current_y + 100)

    left_eye = sd.get_point(current_x + 50, current_y + 60)
    right_eye = sd.get_point(current_x + 100, current_y + 60)

    smile_lc = sd.get_point(current_x + 60, current_y + 25)
    smile_rc = sd.get_point(current_x + 90, current_y + 25)

    smile_ll = sd.get_point(current_x + 40, current_y + 35)
    smile_rl = sd.get_point(current_x + 60, current_y + 25)

    smile_lr = sd.get_point(current_x + 90, current_y + 25)
    smile_rr = sd.get_point(current_x + 110, current_y + 35)

    sd.line(smile_lc, smile_rc, color=color, width=4)
    sd.line(smile_ll, smile_rl, color=color, width=4)
    sd.line(smile_lr, smile_rr, color=color, width=4)

    sd.ellipse(bot_l, top_r, color=color, width=4)
    sd.circle(left_eye, radius=6, width=1, color=color)
    sd.circle(right_eye, radius=6, width=1, color=color)


for i in range(10):
    x = rand.randrange(0, 450, 50)
    y = rand.randrange(0, 450, 50)
    draw_smile(x, y, sd.random_color())

sd.pause()

