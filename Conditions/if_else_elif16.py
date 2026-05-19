#16. Write a program to find largest among four numbers.

num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))
num3 = int(input("Enter num3 "))
num4 = int(input("Enter num4 "))

# Example logic using if-elif-else
if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
   print(" largest = num1 ") 
elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
     print(" largest = num2 ") 
elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
     print(" largest = num3 ") 
else:
     print(" largest = num42 ") 

