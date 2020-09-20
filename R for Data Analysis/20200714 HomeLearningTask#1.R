# Home Learning Task #1
# Author: Gavita Regunath
# Date: 14/07/2020
# Function: Write a R program to create three vectors a,b,c with 5
# integers. Combine the three vectors to become a 3 × 5
# matrix where each column represents a vector. Print the
# content of the matrix. Plot a graph and label correctly.

# Declare three vectors
vec1 = c(1,2,3,4,5) # function c combines the individual numbers into a vector
vec2 = (6:10)  # Shortcut for creating vectors  
vec3 = rep(1,5) #	Create vector by repeating elements of 1 5 times each

# Combine three vectors to a 3 x 5 matrix
mat1 = cbind(vec1,vec2,vec3)

#Print the content of the matrix
print(mat1)

# Plot a graph and label correctly
matplot(mat1,type="p", main="Plot of values in created matrix",xlab="nrows",ylab="ncol")

