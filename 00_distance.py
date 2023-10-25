#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {
    "Moscow On London": ((sites.get("Moscow")[0] - sites.get("London")[0]) ** 2 + (sites.get("Moscow")[1] - sites.get("London")[1]) ** 2) + 0.5,
    "Moscow On Paris": ((sites.get("Moscow")[0] - sites.get("Paris")[0]) ** 2 + (sites.get("Moscow")[1] - sites.get("Paris")[1]) ** 2) * 0.5,
    "London On Paris": ((sites.get("London")[0] - sites.get("Paris")[0]) ** 2 + (sites.get("London")[1] - sites.get("Paris")[1]) ** 2) * 0.5
}

# TODO здесь заполнение словаря

print(distances)




