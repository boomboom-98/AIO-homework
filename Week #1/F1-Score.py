#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise #1
def Eval_F1_Score(tp,fp,fn):
    if type(tp) != int or type(fp) != int or type(fn) != int: # Check type
        print("Input must be type int.")
    if tp <= 0 or fp <= 0 or fn <= 0:
        print(" tp and fp and fn must be greater than zero.")
    else:
        precision = tp/(tp + fp)    # Calculate precision
        recall = tp / (tp + fn)     # calculate recall
        F1_score = 2 * ((precision*recall) / (precision+ recall)) # calculate F1-score
        print(f" F1 score: {F1_score}")
        print(f"precision: {precision}")
        print(f" Recall: {recall}")
        return tp, fn,fp
#Test case
Eval_F1_Score(1,2,3)
Eval_F1_Score('a',2,3)
Eval_F1_Score(-1,4,5)
Eval_F1_Score(0,2,4)


# In[ ]:




