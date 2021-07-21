#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zhang Chi

# PSO算法
import numpy as np
from matplotlib import pyplot as plt 
 
 
class PSO(object):
    def __init__(self, population_size, max_steps):
        self.w = 0.6  # 惯性权重
        self.c1 = self.c2 = 2
        self.population_size = population_size  # 粒子群数量
        self.dim = 2  # 搜索空间的维度
        self.max_steps = max_steps  # 迭代次数
        self.x_bound = [-10, 10]  # 解空间范围
        self.x = np.random.uniform(self.x_bound[0], self.x_bound[1],
                                   (self.population_size, self.dim))  # 初始化粒子群位置
        self.v = np.random.rand(self.population_size, self.dim)  # 初始化粒子群速度
        fitness = self.calculate_fitness(self.x)
        self.p = self.x  # 个体的最佳位置
        self.pg = self.x[np.argmin(fitness)]  # 全局最佳位置
        self.individual_best_fitness = fitness  # 个体的最优适应度
        self.global_best_fitness = np.min(fitness)  # 全局最佳适应度
 
    def calculate_fitness(self, x):
        return np.sum(np.square(x), axis=1)
 
    def evolve(self):
        fig = plt.figure()
        for step in range(self.max_steps):
            r1 = np.random.rand(self.population_size, self.dim)
            r2 = np.random.rand(self.population_size, self.dim)
            # 更新速度和权重
            self.v = self.w*self.v+self.c1*r1*(self.p-self.x)+self.c2*r2*(self.pg-self.x)
            self.x = self.v + self.x
            plt.clf()
            plt.scatter(self.x[:, 0], self.x[:, 1], s=30, color='k')
            plt.xlim(self.x_bound[0], self.x_bound[1])
            plt.ylim(self.x_bound[0], self.x_bound[1])
            plt.pause(0.01)
            fitness = self.calculate_fitness(self.x)
            # 需要更新的个体
            update_id = np.greater(self.individual_best_fitness, fitness)
            self.p[update_id] = self.x[update_id]
            self.individual_best_fitness[update_id] = fitness[update_id]
            # 新一代出现了更小的fitness，所以更新全局最优fitness和位置
            if np.min(fitness) < self.global_best_fitness:
                self.pg = self.x[np.argmin(fitness)]
                self.global_best_fitness = np.min(fitness)
            print('best fitness: %.5f, mean fitness: %.5f' % (self.global_best_fitness, np.mean(fitness)))
 
 
pso = PSO(100, 100)
pso.evolve()
plt.show()

def demo_func(x):
    x1, x2, x3 = x
    return x1 ** 2 + (x2 - 0.05) ** 2 + x3 ** 2
from  sko.GA import GA
ga = GA(func=demo_func, lb=[-1, -10, -5], ub=[2, 10, 2], max_iter=500)
best_x, best_y = ga.run()


# SGD算法
# from sympy import *

# #创建多项式
# def f(x,y):
#     return x**2+y**2

# #梯度下降法
# def gradient_descent(f):
#     x,y=symbols('x y', real=True)
#     dx=diff(f(x,y),x) #求梯度
#     dy=diff(f(x,y),y)
#     alpha=0.1 #学习率
#     max_steps=1000 #最大迭代次数
#     x0,y0=1,3 #初值
#     f0=f(x0,y0) #计算初值代入时的函数值
#     for i in range(1,max_steps):
#         x1=x0-alpha*dx
#         y1=y0-alpha*dy
#         x1=x1.subs(x,x0) #symbol计算转换为数值计算
#         y1=y1.subs(y,y0)
#         f1=f(x1,y1)
#         if (f0-f1)<10e-10: #设定停止迭代阈值
#             break
#         x0,y0,f0=x1,y1,f1 #更新
#     return x1,y1,f1

# x1,y1,f1=gradient_descent(f)
# print(x1,y1,f1)