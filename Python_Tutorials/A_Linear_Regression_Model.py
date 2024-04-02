import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Load the data
try:
    Dframe = pd.read_csv('Python_Tutorials\diamond.csv')
except FileNotFoundError:
    print("The file 'diamond.csv' does not exist in the current directory.")
    exit(1)

#Returns the first n rows & columns of the dataframe.
print(Dframe.head())

print("\n")
print("SHOWCASING THE INFO OF THE DATAFRAME")
Dframe.info()

print("\n")
X = Dframe["carat"]
Xc = Dframe["carat"]
Y = Dframe["price"]

#Printing our two variables we are going to use for the Linear regression.
print("Carat: ", X)
print("\n")
print("Price:", Y)

#INTRODUCE A CONSTANT VALUE TO THE CARAT VARIABLE which is a column of 1s as required by OLS Model
Xc = sm.add_constant(Xc)
print(Xc.head())

#Performing the Ordinary Least Squares (OLS) method
OLS_LinearRegression = sm.OLS(endog=Y, exog=X).fit()
print(OLS_LinearRegression.summary())

#Plotting the data
plt.plot(X, Y, '*')

#fitting the line of best fit and finding m&b
m, b = np.polyfit(X, Y, 1)

#Plotting the line of best fit
plt.plot(X, m*X + b,)

#Labelling the graph
plt.xlabel("Carat")
plt.ylabel("Price")
plt.title("Price vs Carat")
#Displaying the graph with grids
plt.grid()
plt.show()

# Adding a heatmap to the graph to show the correlation between the variables
plt.figure(figsize=(10, 8))
sns.heatmap(Dframe.corr(), annot=True, cmap='coolwarm')
plt.show()