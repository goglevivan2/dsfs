# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:30:42 2019

@author: Dell
"""
import linalgebra_vectors
#### СТАТИСТИКА ####
from matplotlib import pyplot as plt
import random
from collections import Counter
import math


num_friends=[]
for i in range(204):
    num_friends.append(random.randint(20,500))
print('Число друзей: \n')
print(num_friends)

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs,ys)
plt.axis([0,101,0,25])
plt.title('Гистограмма количества друзей')
plt.xlabel('Количество друзей')
plt.ylabel('Количество людей')
plt.show()
# Формирование статистик
num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)
print('Максимальное значение:',largest_value)
print('Минимальное значение:',smallest_value)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

print(sorted_values)
print(smallest_value)
print(second_smallest_value)
print(second_largest_value)


# Показатели центра распределения

def mean (x):
    return sum(x)/len(x)

print('Среднее :',mean(num_friends))

# медиана
x = [1,2,3,5,4,5]
x= sorted(x)
print('Mediana: ',x[5//2]) #или x[2] если точек в векторе 6 то медиана ср. арифм. x[2] и x[3]
 
def median(v):
    '''Возвращает ближайшее к середине значение для v '''
    n = len(v)
    sorted_v=sorted(v)
    midpoint = n//2
    
    if n%2 == 1:
        #если нечётное, то вернуть среднее значение
        return sorted_v[midpoint]
    else:
        #если чётное вернуть среднее двух значений
        lo = midpoint - 1
        hi = midpoint
        return(sorted_v[lo]+sorted_v[hi])/2

print("Медиана значений: ",median(num_friends))
test = [1,2,3,4]
print("Медиана test: ",median(test))

#квантиль

def quantile(x,p):
    ''' Возвращает значение в x, соответствующее p-ому проценту данных'''
    p_index = int(p*len(x)) # преобразует значение % в индекс списка
    return sorted(x)[p_index]
print(quantile(num_friends,0.15))
# мода - значение, которое встречается наиболее часто

def mode(x):
    ''' Возвращает список, так как мод может быть больше одной'''
    counts = Counter(x)
    max_count= max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]
print(mode(num_friends))
h =[1,2,2,3,4]
print(mode(h))
    
#### ПОКАЗАТЕЛИ ВАРИАЦИИ ####

#размах

def data_range(x):
    return max(x)-min(x)

print("Размах",data_range(num_friends))
print("Размах h ",data_range(h))

# вектор отклонения от среднего (центрировать вектор)
def de_mean(x):
    '''Пересчитать x, вычтя из него среднее '''
    x_bar = mean(x)
    return[x_i-x_bar for x_i in x]
    
#дисперсия
def variance(x):
    ''' Предполагается что вектор x состоит минимум из 2-х элементов'''
    n=len(x)
    deviations = de_mean(x)
    zn = linalgebra_vectors.sum_of_squares(deviations)
    return zn/(n-1)

print ('Dispersia',variance(num_friends))

    
# стандартное отклонение
def standard_deviation(x):
    return math.sqrt(variance(x))
print('Стандартное отклонение:',standard_deviation(num_friends))

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)
print('интерквантильный размах:',interquartile_range(num_friends))
# КОРРЕЛЯЦИЯ

daily_minutes=[]
for i in range(204):
    daily_minutes.append(random.randint(20,40))

#ковариация
    
def covariance(x,y):
    n = len(x)
    return linalgebra_vectors.dot(de_mean(x),de_mean(y))/n-1

print('ковариация:',covariance(num_friends, daily_minutes))

# корреляция

def correlation(x,y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x,y) / stdev_x / stdev_y
    else:
        return 0 # если переменные не меняются то корреляция равна 0
    
print('корреляция:',correlation(num_friends, daily_minutes))

# игнорирование выброса

outlier = num_friends.index(50)

# отфильтровать выброс

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]
daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]
print('корреляция1:',correlation(num_friends, daily_minutes))    
print('корреляция2:',correlation(num_friends_good, daily_minutes_good))    
    