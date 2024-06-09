#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math

def is_number(n):  # Function check type x
    try:
        float(n)  # Doi gia tri cua x sang kieu float
        # chi gia tri int va float moi chay duoc code float(n)
        # Kieu du lieu khac thi se hien loi "ValueError"
    except ValueError:
        return False
    return True

    # Sigmoid, ReLU, ELU
    def sigmoid(x):
        return 1 / (1 + math.e(-x))
    def ReLU(x):
        if x > 0 :
            return x
        if x <= 0:
            return 0
    def ELU(x,alpha = 1):
        if x > 0:
            return x
        if x <= 0:
            return alpha * (math.e(-x) - 1)

    def activation_function():
        x = int(input(" Enter a number: "))
        if is_number(x) == False:
            print(" x must be a number.")
        func_type = input("Input activation function (sigmoid,ReLU,ELU")
        if func_type.lower() not in [" sigmoid", "relu", "elu"]:
            print(f"{func_type} is not supported")
        if func_type.lower() == "sigmoid":
            print(f"Sigmoid({x}) = {sigmoid(x)}")
        elif func_type.lower() == "relu":
            print(f"ReLU({x}) = {relu(x)}")
        else:
            print(f"ELU({x}) = {elu(x)}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




