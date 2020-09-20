# Home Learning Task #4
# Author: Gavita Regunath
# Date: 15/07/2020
# Function: Import the GGPLOT 2 library and plot a graph using the qplot function.
# X axis is the sequence of 1:20 and the y axis is the x ^ 2. Label the graph appropriately.

# Create vector of heights of school children
height = c(50,102,99,108,80)

#Plot bar chart
barplot(height,
        main = "Height of school children in Bubble #1",
        xlab = "Children",
        names.arg = c("Jack", "Isla", "Charlote", "Lucy", "Caelan"),
        ylab = "Height (cm)",
        border="red",
        col="blue",
        density=10)


