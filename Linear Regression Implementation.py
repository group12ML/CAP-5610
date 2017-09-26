import pandas as pd
import numpy as np
from excelToArray import excelToArray
from sklearn.metrics import r2_score

# Load the airfoil dataset
airfoil = excelToArray()

# Separates the data into the input and output values
X = airfoil[:,:6]
Y = airfoil[:, 6]

# Seperating the data into training and testing sets
# We used about 80% of the data as training data
train_X = X[0:1201]
test_X  = X[1201:]

train_Y = Y[0:1201]
test_Y  = Y[1201:]

# Implementing the normal equation
weight = np.linalg.inv(train_X.transpose().dot(train_X)).dot(train_X.transpose().dot(train_Y))

# Printing the resulting weights
print "Coefficients: \n", weight

# Create an array containing the predicted y values
predict_Y = test_X.dot(weight)

# Calculate and print variance for comparisson purposes
print "variance: ", r2_score(test_Y, predict_Y)
