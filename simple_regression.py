# Simple Linear Regression


import pandas as pd                  
import numpy as np                  
import matplotlib.pyplot as plt        


# Importing the dataset 
dataset = pd.read_csv('Salary_Data.csv')  
x = dataset.iloc[:, :-1].values    
y = dataset.iloc[:, 1].values    
 
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)
