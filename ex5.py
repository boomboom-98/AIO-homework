# -*- coding: utf-8 -*-
"""ex5

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LVBXdXGRawKtahURojTrZi0Gy9q6e64W
"""

#Viết function thực hiện Mean Difference of n_th Root Error

#copy from TN.ex13
def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1/ n )
    y_hat_root = y_hat ** (1/ n )
    difference = y_root - y_hat_root
    loss = difference ** p

    return loss