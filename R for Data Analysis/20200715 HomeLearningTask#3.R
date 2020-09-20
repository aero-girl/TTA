# Home Learning Task #3
# Author: Gavita Regunath
# Date: 15/07/2020
# Function: Import the GGPLOT 2 library and plot a graph using the qplot function.
# X axis is the sequence of 1:20 and the y axis is the x ^ 2. Label the graph appropriately.

# Include ggplot2 library
library(ggplot2)

# Define x and y
x = 1:20
y = x^2

# Plot graph
qplot(x,y,main="Home Learning Task #3",xlab = "x-axis",ylab = "y-axis")


