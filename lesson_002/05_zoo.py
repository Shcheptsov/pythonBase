#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')
print(zoo)
# добавьте птиц в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)
#  и выведите список на консоль

# уберите слона
zoo.remove('elephant')
#  и выведите список на консоль
print(zoo)

# выведите на консоль в какой клетке сидит обезьяна (monkey)
# и жаворонок (lark). Номера при выводе должны быть понятны простому человеку, не программисту.
print('Обезьяна сидит в клетке', zoo.index('monkey')+1)
print('жаворонок сидит в клетке', zoo.index('lark')+1)

