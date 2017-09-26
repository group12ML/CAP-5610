import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import r2_score
from excelToArray import excelToArray

# Load the airfoil dataset
airfoil = excelToArray()

# Change the values here to change which columns are x's/y's
airfoil_X = airfoil[:, :-1]
airfoil_Y = airfoil[:, 6]

# Split the data into training/testing sets (divides the rows)
airfoil_X_train = airfoil_X[0:1201]
airfoil_X_test = airfoil_X[1201:]

# Split the targets into training/testing sets
airfoil_y_train = airfoil_Y[0:1201]
airfoil_y_test = airfoil_Y[1201:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(airfoil_X_train, airfoil_y_train)

# Make predictions using the testing set
airfoil_y_pred = regr.predict(airfoil_X_test)

# Print the resulting weights
regr.coef_[0] = regr.intercept_     # Sklearn doesn't include the intercept in the coefficients, we changed that
print "Coefficients: \n", regr.coef_

# Calculate and print the variance
print "Variance score: %.2f" % r2_score(airfoil_y_test, airfoil_y_pred)

