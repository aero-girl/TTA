# Challenge #2
# Author: Gavita Regunath
# Date: 15/07/2020
# Function: Write a R program to print the numbers from 1 to 100 and
# print "Fizz" for multiples of 3, print "Buzz" for multiples of 5,
# and print " FizzBuzz " for multiples of both.

# Declare vector of numbers from 1 to 100
numbers = 1:100

# Print numbers
for (n in numbers) 
  {
  # number divisible by 3, print 'Fizz'
  if (n %% 3 == 0) 
  {print("Fizz")}
  
   # number divisible by 5, print 'Buzz' 
  else if (n %% 5 == 0) 
  {print("Buzz")}
  
  # number divisible by both 3 & 5, print 'FizzBuzz'
  else if (n %% 3 == 0 & n %% 5 == 0) 
  {print("FizzBuzz")}
  
  else print(n)
  }
