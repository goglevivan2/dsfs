# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:18:41 2019

@author: Dell
"""
import random
import math
from matplotlib import pyplot as plt
from collections import Counter
def random_kid():
    return random.choice(["boy","girl"])

# boy and girl paradox
 
both_girls = 0
older_girl = 0
either_girl = 0

for _ in range(100000):
    younger = random_kid()
    older = random_kid()
    if older == "girl": # старшая?
        older_girl +=1
    if older == "girl" and younger == "girl": # обе?
        both_girls +=1
        
    if( older == "girl" or younger == "girl"):
        either_girl +=1
        
print("P(обе | старшая):", both_girls/ older_girl)
print("P(обе | любая)", both_girls/either_girl )
        
# ДФР равномерного распределения
def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

#ИФР равномерного распределения
def uniform_cdf(x):
    """ Возвращает вероятность того, что равномерно распределённая 
    случайная величина <= x """
    if x < 0 : return 0
    elif x < 1 : return x
    else : return 1
# Нормальное распределение

# ДФР нормального распределения
def normal_pdf(x, mu = 0, sigma = 1):
    sqrt_two_pi = math.sqrt(2*math.pi)
    return (math.exp(-(x-mu) ** 2 /2 / sigma ** 2)/(sqrt_two_pi*sigma))

xs = [x/10.0 for x in range(-50,50)]
plt.plot(xs,[normal_pdf(x,sigma = 1)for x in xs],'-',label='мю =0 , сигма = 1')
plt.plot(xs,[normal_pdf(x,sigma = 2)for x in xs],'--',label='мю =0 , сигма = 2')
plt.plot(xs,[normal_pdf(x,sigma = 0.5)for x in xs],':',label='мю =0 , сигма = 0.5')
plt.plot(xs,[normal_pdf(x,mu = -1)for x in xs],'-.',label='мю =-1 , сигма = 1')
plt.legend()
plt.title("Несколько ДФР нормального распределения")
plt.show()

# ИФР нормального распределения 
def normal_cdf(x,mu=0,sigma=1):
    return (1+ math.erf((x-mu)/math.sqrt(2)/sigma))/2

xs = [x/10.0 for x in range(-50,50)]
plt.plot(xs,[normal_cdf(x,sigma = 1)for x in xs],'-',label='мю =0 , сигма = 1')
plt.plot(xs,[normal_cdf(x,sigma = 2)for x in xs],'--',label='мю =0 , сигма = 2')
plt.plot(xs,[normal_cdf(x,sigma = 0.5)for x in xs],':',label='мю =0 , сигма = 0.5')
plt.plot(xs,[normal_cdf(x,mu = -1)for x in xs],'-.',label='мю =-1 , сигма = 1')
plt.legend(loc=4) #внизу справа
plt.title("Несколько ИФР нормального распределения")
plt.show()    

# обратная ИФР нормального распределения 
# (tolerance - это константа точности)

def inverse_normal_cdf(p,mu=0,sigma=1,tolerance=0.00001):
    """найти приближённую инверсию используя двоичный поиск"""
    # если не стандартизировано, то стандартизировать и прошкалировать
    if mu != 0 or sigma !=1:
        return mu+sigma*inverse_normal_cdf(p,tolerance=tolerance)
    
    low_z, low_p = -10.0 , 0
    hi_z , hi_p = 10.0 , 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z)/2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            # значение середины всё ещё слишком низкое, искать выше его
            low_z , low_p = mid_z , mid_p
        elif mid_p > p:
             # значение середины всё ещё слишком высокое, искать ниже
             hi_z , hi_p = mid_z , mid_p
        else:
            break
        return mid_z
    
    



#Центральная предельная теорема
        
# независимое испытание Бернулли, в котором имеется всего 
# два исхода (1 и 0) с постоянной вероятностью
        
def bernoulli_trial(p):
    return 1 if random.random() < p else 0

# биномиальное распределение
def binomial(n,p):
    return sum(bernoulli_trial(p) for _ in range(n))

# Построить гистограмму
def make_hist(p, n, num_points):
    data =[binomial(n,p) for af in range(num_points)]
    # столбчатая диаграмма, показывающая фактические биномиальные выборки
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
             [v / num_points for v in histogram.values()],
             0.8,
             color='0.75')
    mu = p*n
    sigma = math.sqrt(n*p*(1-p))
    
    # линейный график, показывающий нормальное приближение
    xs = range(min(data),max(data)+1)
    ys = [normal_cdf(i+0.5,mu,sigma)-normal_cdf(i-0.5,mu,sigma)
    for i in xs]
    plt.plot(xs,ys)
    plt.title("Биномиальное распределение и его нормальное приближение")
    plt.show()

make_hist(0.75,100,10000)    