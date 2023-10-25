#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Отец", "Мать", "Сестра"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    [my_family[0], 180],
    [my_family[1], 165],
    [my_family[2], 145]
]

print("Росто", my_family_height[0][0], "-", my_family_height[0][1], "См");
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

family_height = 0;

for family in my_family_height:
    family_height += family[1]

print(family_height);