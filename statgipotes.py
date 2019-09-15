# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:07:43 2019

@author: Dell
"""
import math
import teoryofchances
#аппроксимация биноминальной случайной величины нормальным распределением
def normal_approximation_to_binomial(n,p):
    """находит mu и sigma, которые соответствуют binomial(n,p)"""
    mu = p * n
    sigma = math.sqrt(p*(1-p)*n)
    return mu, sigma
#вероятность,что значение нормальной случайной величины 
#ниже порогового значения 
normal_probability_below = teoryofchances.normal_cdf

#оно выше порогового значения, если оно не ниже порогового значения
def normal_probability_above(lo,mu=0,sigma=1):
    return 1 - teoryofchances.normal_cdf(lo,mu,sigma)

#оно лежит между, если оно меньше hi, но не ниже lo
def normal_probability_between(lo,hi,mu=0,sigma=1):
    return teoryofchances.normal_cdf(hi,mu,sigma) - teoryofchances.normal_cdf(lo,mu,sigma)

# оно лежит за пределами, если оно не внутри
def normal_probability_outside(lo,hi,mu=0,sigma=1):
    return 1 - normal_probability_between(lo,hi,mu,sigma)