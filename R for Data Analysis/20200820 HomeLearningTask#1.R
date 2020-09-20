# Home Learning Task
# Author: Gavita Regunath
# Date: 20/08/2020
# Function: Using the ggplot in-built data sets in RStudio and the qplot
# function, get your creative juices flowing and create a meaningful
# and impactful data visualization using your preferred data set.

# Include ggplot2 library
library(ggplot2)

#data("msleep")
# msleep- contains information about sleep and awake times of different mammals

# Figure showing the relationship between total amount of awake vs body weight
# Coloured by species
fig1 = ggplot(msleep, aes(x = bodywt, y = awake, color = vore)) 
fig1 = fig1 + geom_point()
fig1 = fig1 + ggtitle("Total amount of awake vs body weight")
fig1

# Figure showing the relationship between total amount of sleep vs body weight
# Coloured by species
fig2= ggplot(msleep, aes(x = bodywt, y = sleep_total, color = vore))
fig2 = fig2 + geom_point() 
fig2 = fig2 + ggtitle("Total amount of sleep vs body weight")
fig2

# Figure showing the relationship between total amount of sleep vs body weight
# Facet data (partitions a plot into a matrix of panels)
fig3 = ggplot(msleep, aes(x = bodywt, y = sleep_total, color = vore)) 
fig3 = fig3 + geom_point(size = 3) 
fig3 = fig3 + facet_wrap(~vore)
fig3 = fig3 + xlab("Body Weight") + ylab("Total Sleep") + ggtitle("Sleep Data partitioned into species")  
fig3

# Plot total number of species within each group of species
# table(msleep$vore)
fig4 = ggplot(msleep, aes(x=vore,fill=vore)) 
fig4 = fig4 +  geom_bar() 
fig4 = fig4 +labs(x='Species', y='Number of Species')
fig4
# Dataset contains more herbivores than any other species

meancom =rep_len(mean(msleep$sleep_total), length(msleep$vore))
# Box plot of total sleep time of species, showing min, max and median stats of each vore
fig5 = ggplot(msleep, aes(x = vore, y = sleep_total, fill = vore)) 
fig5 = fig5 + geom_boxplot()
fig5 = fig5 + labs(title = 'On average, insects sleep more than other species'
                   ,x = 'Species' ,y = 'Total amount of sleep (hours)')
fig5
# On average, insects sleeps more than other species


