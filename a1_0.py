import time
import timeit
from tkinter import N
from turtle import title
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from pythonds3.basic import Stack
# def sum_of_n(n):
#     the_sum = 0
#     for i in range(1, n + 1):
#         the_sum += i
#     return the_sum


# # Measure the time taken by the function
# def sum_of_n_time(n):
#     start_time = time.time()
#     the_sum = sum_of_n(n)
#     end_time = time.time()
#     return the_sum, end_time - start_time
# # Example usage:


# for i in range(5):
#     print("sum is %d required %10.7f seconds" % sum_of_n_time(10000))

# list
# def test1():
#     l = []
#     for i in range(1000):
#         l = l + [i]

# def test2():
#     l = []
#     for i in range(1000):
#         l.append(i)
# def test3():
#     l = [i for i in range(1000)]
# def test4():
#     l = list(range(1000))

# for func in (test1, test2, test3, test4):
#     t1 = time.time()
#     func()
#     t2 = time.time()
#     result = t2 - t1
#     print(f"{func.__name__} took {result:.7f} seconds")




# # 初始化用于存储 x 和 pzt 的列表
# x_values = []
# pzt_values = []
# pte_values = []
# pop_zero = timeit.Timer("x.pop(0)", "from __main__ import x")
# pop_end = timeit.Timer("x.pop()", "from __main__ import x")
# print(f"{'n':>15}{'pop(0)':>15}{'pop()':>15}")
# for i in range(1000000, 10000001, 1000000):
#     x = list(range(i))
#     pzt = pop_zero.timeit(number=1000)
    
#     x_values.append(i)
#     pzt_values.append(pzt)
    
#     x = list(range(i))
#     pte = pop_end.timeit(number=1000)
#     pte_values.append(pte)
    
#     print(f"{i:>15d}{pzt:>15.5f}{pte:>15.5f}")

# # 定义拟合函数，这里以1次函数为例
# def func(x, a, b):
#     return a * x + b

# # 对 pzt_values 进行曲线拟合
# popt_pzt, _ = curve_fit(func, x_values, pzt_values)
# pzt_fit = func(np.array(x_values), *popt_pzt)

# # 对 pte_values 进行曲线拟合
# popt_pte, _ = curve_fit(func, x_values, pte_values)
# pte_fit = func(np.array(x_values), *popt_pte)
# print(popt_pzt)
# print(popt_pte)
# # 绘制拟合曲线
# plt.plot(x_values, pzt_fit, label='pzt fit curve')
# plt.plot(x_values, pte_fit, label='pte fit curve')

# # 添加图例
# plt.legend()

# # 绘制散点图
# plt.scatter(x_values, pzt_values)
# plt.scatter(x_values, pte_values)
# plt.xlabel('x_values')
# plt.ylabel('times')
# plt.title('Scatter Plot of x_values and times')
# plt.show()

# x1 = []
# y1 = []
# for i in range(100):
#     start = time.time()
#     for j in range(100):
#         k = 2 + 2
#     end = time.time()
#     x1.append(i)
#     y1.append(end - start)



# plt.scatter(x1, y1)
# plt.show()
# 栈
# class Stack:
#     def __init__(self):
#         self.items = []
#     def is_empty(self):
#         return self.items == []
#     def push(self, item):
#         self.items.append(item) 
#     def pop(self):
#         return self.items.pop() 
#     def peek(self):
#         return self.items[len(self.items) - 1]
#     def size(self):
#         return len(self.items)

# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())

def divideBy2(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
    binString = ""
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())
    return binString
print(divideBy2(233))
# 队列
class queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

from pythonds3.basic import Queue

def hotPotato(name_list,num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))