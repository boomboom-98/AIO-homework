#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Viết 4 functions để ước lượng các hàm số sau sin x, cos x, sinh x, cosh x
import math
def factorial(n):
    if n <= 0:
        print("n must be greater than 0")
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def sin(x, n):
    if n <= 0:
        print("n must be greater than 0")
    else:
        sum = (((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(n))
    return sum

def cos(x, n):
    if n <= 0:
        print("n must be greater than 0")
    else:
        sum = (((-1) ** i) * (x ** (2 * i)) / factorial(2 * i) for i in range(n))
    return sum

def sinh(x, n):
    if n <= 0:
        print("n must be greater than 0")
    else:
        sum((x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(n))
    return sum

def cosh(x, n):
    if n <= 0:
        print("n must be greater than 0")
        sum((x ** (2 * i)) / factorial(2 * i) for i in range(n))
    return sum

if __name__ == "__main__":
    x = float(input('Enter x (radian (0,2pi]): '))
    n = int(input('Enter n (int): '))

    if x > 0 and x <= 2 * math.pi:
        print(f'appox sin x:{x}, n:{n} = {sin(x, n)}')
        print(f'appox cos x:{x}, n:{n} = {cos(x, n)}')
        print(f'appox sinh x:{x}, n:{n} = {sinh(x, n)}')
        print(f'appox cosh x:{x}, n:{n} = {cosh(x, n)}')


# In[ ]:




