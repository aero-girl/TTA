# Challenge #1
# Author: Gavita Regunath
# Date: 15/07/2020
# Function: Write a R program to get the first 10 Fibonacci numbers.

# Fibonacci sequence to the first 10 numbers
n =10

# Instantiate fib vector
fib = numeric(n)

# Declare first two sequence in the Fibonacci sequence
fib[1] = 0
fib[2] = 1

# Create for loop to recursively work out the Fibonacci sequence
for (i in 3:n) 
  { 
  fib[i] = fib[i-1]+fib[i-2]
  } 

# Display the Fibonacci sequence to the first 10 numbers
print(fib)