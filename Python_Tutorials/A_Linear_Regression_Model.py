import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Load the data
try:
    Dframe = pd.read_csv('diamond.csv')
except FileNotFoundError:
    print("The file 'diamond.csv' does not exist in the current directory.")
    exit(1)

print(Dframe.head())