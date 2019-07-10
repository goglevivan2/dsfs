# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:12:25 2019

@author: Dell
"""
import math
######### ВЕКТОРЫ ##########
height_weight_age = [175, # сантиметры
                     68,  # киллограмы
                     40]  # годы

grades = [95, # экзамен1
          80, # экзамен2
          75] # экзамен3
 
# сложение 
def vector_add(v,m):
    '''
    Складывает векторы
    '''
    return [v_i + m_i for v_i,m_i in zip(v,m)]

print(vector_add(height_weight_age,grades))
test = []
test = vector_add(height_weight_age,grades)

# вычитание
def vector_subtract(v, w):
    '''
    вычитает соответствующие элементы
    '''
    return [v_i - w_i for v_i,w_i in zip(v,w)]

print(vector_subtract(test,height_weight_age ))

# покомпонентная сумма вектора
def vector_sum(vectors):
    '''
    Суммирует все соответствующие элементы
    '''
    return reduce(vector_add,vectors)

#print(vector_sum([1,2,3,4,5,6,7,8,9]))
#TypeError: zip argument #1 must support iteration
    
# умножение вектора на скаляр
def scalar_multiply(c,v):
    ''' c - число, v - вектор'''
    return[c*v_i for v_i in v]

print(scalar_multiply(10,grades))

# скалярное произведение

def dot(v,w):
    ''' v_1*w_1+....+v_n*w_n '''
    return sum(v_i*w_i for v_i,w_i in zip(v,w))

print(dot(height_weight_age,grades))

# cумма квадратов
def sum_of_squares(v):
    return dot(v,v)    
print(sum_of_squares(height_weight_age))

# длинна вектора
def magnitude(v):
    return math.sqrt(sum_of_squares(v))
print(magnitude(height_weight_age))
   
# эвклидово расстояние 
def distance(v,w):
    return(magnitude(vector_subtract(v,w)))

print(distance(height_weight_age,grades))
