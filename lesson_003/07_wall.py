# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for current_y in range(12):
    for current_x in range(7):
        offset = 0 if current_y % 2 else 50
        bottom_left = sd.get_point(offset + current_x * 100 - 50, 0 + current_y * 50)
        top_right = sd.get_point(offset + 50 + current_x * 100, 50 + current_y * 50)
        sd.rectangle(bottom_left, top_right, color=sd.COLOR_DARK_RED, width=3)

sd.pause()

sd.pause()
