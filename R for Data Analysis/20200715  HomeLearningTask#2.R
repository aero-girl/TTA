# Home Learning Task #2
# Author: Gavita Regunath
# Date: 15/07/2020
# Function: Write a R program to create a Data frames which contain details of
# employees and display the details.  (Name, Age, Gender, Role and Length of service).

# Declare Name vector
Name = c("Isla", "Caelan", "Charlotte", "Jack")
Age = c(9,6,8,6)
Gender = c("F","M","F","M")
Role = c("Student","Student","Student","Student")
LenghtOfService = c("4","2","4","2")

# Create data frame
Employees = data.frame(Name,Age,Gender,Role,LenghtOfService)

# Display data frame
print(Employees)

