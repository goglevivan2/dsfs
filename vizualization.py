# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:57:50 2019

@author: Dell
"""

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010] # годы
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3] # ввп

# создание линейной диаграммы : годы по оси X, ввп по оси Y
plt.plot(years, gdp, color = 'red', linestyle = 'solid') # в отличии от книги параметр market не нужен



# добавление названия диаграммы
plt.title("Номинальный ВВП")

# добавление подписи к оси Y
plt.ylabel("Млрд $")

# добавление подписи к оси X
plt.xlabel("Годы")

# отображение диаграммы
plt.show()
print('\a')