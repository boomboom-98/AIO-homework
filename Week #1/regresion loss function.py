#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Viết function lựa chọn regression loss function để tính loss:
import math
import random

num_samples = input('Input number of samples (integer number) which are generated: ')

if num_samples.isnumeric() == int :
    print('Number of samples must be an integer number.')
    return
num_samples = int(num_samples)
loss_name = input('Input loss name (MAE|MSE|RMSE): ')
if loss_name.lower() not in ["mae", "mse", "rmse"]:
    print(f'{loss_name} is not supported to calculate loss function.')
    
if loss_name.lower() == "mae":
    for i in range(num_samples):
    sum = 0
    y = (random.uniform(0, 10)
    y_hat = random.uniform(0, 10)
    abs_error = abs(y - y_hat)
    sum = sum + abs_error
    mae = sum/n
if loss_name.lower() == "mse":
    for i in range(num_samples):
    sum = 0
    y = (random.uniform(0, 10)
    y_hat = random.uniform(0, 10)
    error = (y - y_hat)**2
    sum = sum + error
    mse = sum/n  
if loss_name.lower() == "rmse":
    for i in range(num_samples):
    sum = 0
    y = (random.uniform(0, 10)
    y_hat = random.uniform(0, 10)
    error = (y - y_hat)**2
    sum = sum + error
    mse = sum/n  
    rmse = math.sqrt(mse)


# In[ ]:




