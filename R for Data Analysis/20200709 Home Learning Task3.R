# Home Learning Task #3
# Author: Gavita Regunath
# Date: 09/07/2020
# Function: Write a R program to create sequence of numbers from 20 to 50. 
# Find the mean of numbers from 20 to 60 and sum of numbers from 51 to 91.

# Declare variables
print("Sequence of numbers from 20 to 50:")
Sequence.number = (20:50)
print(Sequence.number)

# Compute the mean of numbers
Mean.number = mean(20:60)
print(paste("Mean of numbers from 20 to 60:", Mean.number))

# Compute the sum of numbers
Sum.number = sum(51:91)
print(paste("Sum of numbers from 51 to 91:",Sum.number))