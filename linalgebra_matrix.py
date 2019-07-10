# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:32:38 2019

@author: Dell
"""
#################### МАТРИЦЫ #########################
A = [[1,2,3],
    [4,5,6]]

B = [[1,2],
     [3,4],
     [5,6]]

# форма матрицы

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # число элементов в первой строке
    return num_rows, num_cols

print(shape(A))

# получить i-ю строку

def get_row(A,i):
    return A[i]

print(get_row(A,1))

# получить j-й столбец
def get_column(A, j):
    return [A_i[j] for A_i in A]

print(get_column(A,1))

# создание матрицы при наличии её формы и функции (пример единичной матрицы)
'''
def make_matrix(num_rows,num_cols,entry_fn):
    """Возвращает матрицу   num_rows X num_cols, 
    (i,j)-й элемент которой равен entry_fn(i,j)"""
    return [[entry_fn(i, j for j in range(num_cols) ] for i in range(num_rows) ]
 '''
def is_diagonal(i,j):
    '''единицы по диагонали, остальные - нули'''
    return 1 if i == j else 0

#identity_matrix = make_matrix(5,5, is_diagonal)

#print(identity_matrix)
################### ПРИМЕР ИЗ ГЛ № 1 ПРО DataSciencester #################
# пользователь  0 1 2 3 4 5 6 7 8 9
#
friendships = [[0,1,1,0,0,0,0,0,0,0], # пользователь 0
               [1,0,1,1,0,0,0,0,0,0], # пользователь 1
               [1,1,0,1,0,0,0,0,0,0], # пользователь 2
               [0,1,1,0,1,0,0,0,0,0], # пользователь 3
               [0,0,0,1,0,1,0,0,0,0], # пользователь 4
               [0,0,0,0,1,0,1,1,0,0], # пользователь 5
               [0,0,0,0,0,1,0,0,1,0], # пользователь 6
               [0,0,0,0,0,1,0,0,1,0], # пользователь 7
               [0,0,0,0,0,0,1,1,0,1], # пользователь 8
               [0,0,0,0,0,0,0,0,1,0]] # пользователь 9

print(friendships[0][2] == 1)
print(friendships[0][8] == 1)

# поиск связей

friends_of_five = [i for i,is_friend in enumerate (friendships[5]) if is_friend]

print('Друзья человека №5 ',friends_of_five)
  