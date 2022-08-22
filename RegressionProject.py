import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
import seaborn as sns;
import scipy.stats;
from scipy.stats import linregress;
import statistics;
import math

#Read Data and assign variables
estateData = pd.read_csv(r'/Users/aj/Documents/Regression/Real Estate.csv');

#Remove undesired values from dataset
estateData = estateData.drop(['No','X5 latitude','X6 longitude', 'X2 house age', 'X3 distance to the nearest MRT station','X4 number of convenience stores'],axis=1);

#Rename columns to more conventional names
estateData = estateData.rename(columns = {"X1 transaction date":"transactionDate", "Y house price of unit area":"priceUnitArea"});

# Set date values into strings and split to get specific year value
time = estateData['transactionDate'].apply(lambda x:str(x).split(".")); 
years = [int(year[0]) for year in time];
estateData['transactionDate'] = years;

#Show histrogram for normal distribution of dependent variable (price per unit area)
sns.histplot(estateData['priceUnitArea']);
plt.title("Distribution of Price per Unit Area");
plt.show();

#Show lineplot for linear regression
sns.lineplot(x=estateData['transactionDate'], y=estateData['priceUnitArea']);
plt.title("Transaction Date vs. Price per Unit Area");
plt.show();

#Retrieve statistical values
x=estateData['transactionDate'];
y=estateData['priceUnitArea'];
slope, intercept, r_value, p_value, std_err = linregress(x, y);
print("m: ", slope , "\nb: ", intercept, "\nSE: ", std_err, "\nr: ",r_value, "\np: ",p_value);

#t-score
t = slope/std_err;
print("t: ",t);

#sample size
n = len(x);
print("n: ",n);

#mean
mean = statistics.mean(y);
print("mean: ",mean);

#Calculate 95% CI
lowCI = mean-(t*(std_err/math.sqrt(n)));
highCI = mean+(t*(std_err/math.sqrt(n)));
print("95% CI : [",lowCI,",", highCI,"]");
