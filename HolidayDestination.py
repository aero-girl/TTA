#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:04:06 2020
Create a csv file and analyse data
@author: gavita
"""

# Import pandas
import pandas as pd
import matplotlib.pyplot as plt

# Read data from file 'Holiday Destination.csv' 
data = pd.read_csv("Holiday Destination.csv") 

# 1. Get the number of rows and columns
NumberRowCol = data.shape
print("\n 1. The number of rows and columns: ", NumberRowCol)

# 2. Print row 3-8 (using iloc/loc).
print("\n 2. Rows 3-8: \n" , data.iloc[2:8])

# 3.Find the mean number of all -inclusive hotels across all destinations. 
meanValue = data.loc[:,"Number of all-inclusive hotels"].mean()
print("\n3. The mean number of all -inclusive hotels across all destinations is: "\
      , meanValue)

# 4. Find the lowest scoring destination.
minValue = data['Feedback score'].min()
column = data["Feedback score"]
min_index = column.idxmin()
print("\n 4. The lowest scoring destination is:", data.iloc[min_index,0], \
      "with a score of",minValue )

# 5. Find the highest scoring destination.    
maxValue = data["Feedback score"].max()
max_index = column.idxmax()
print("\n 5. The highest scoring destination is:", data.iloc[max_index,0], \
      "with a score of",maxValue )

# 6.Find all the destinations where there are more than 9 inclusive hotels.
Dest9 = data["Destination"].where(data["Number of all-inclusive hotels"] > 9)
print("\n 6. All the destinations where there are more than 9 inclusive hotels.", Dest9)

# 7.Filter the data by destination and score above 8.
MoreThanEight = data["Feedback score"] > 8
DestMoreThanEight = data[MoreThanEight]
PrintDestMoreThanEight = DestMoreThanEight.head()
print("\n 7. All the destinations with feedback score greater that 8:",\
      PrintDestMoreThanEight)

# 8. Filter the data by destination and score below 2
# (I need to know if these destinations should be removed or there is a problem)
LessThanTwo = data["Feedback score"] < 2
DestLessThanTwo = data[LessThanTwo]
PrintLessThanTwo = DestLessThanTwo.head()
print("\n 8. All the destinations with feedback score less than 2:",\
      PrintLessThanTwo)

# 9. Is there a correlation between number of all inclusive hotels and score? 
CorrResult = data["Number of all-inclusive hotels"].corr(data["Feedback score"])
print(" \n 9. The correlation coefficient between number of all inclusive hotels and score is", round(CorrResult,2))
print("The result signifies a weak negative (downhill sloping) linear relationship")

# 10. Create a data visualisation diagram to show destination and highest scores? 
plt.scatter(data["Number of all-inclusive hotels"],data["Feedback score"])
plt.show()
