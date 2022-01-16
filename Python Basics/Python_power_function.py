#Fuction of power
#return  power of any number
def power(num,n):
   return(num**n)

num=int(input("enter number:"))
n=int(input("enter power:"))

#power function calling passing number and power(n)
ans=power(num,n)
print(f"{num} power {n} is {ans}")


#Function of Factorial
# factorial of given number
def factorial(n):
   #when n is less than  0 , factorial is 0
	if n < 0:
		return 0
   #when n is equal to 0 or 1 , factorial is  1

	elif n == 0 or n == 1:
		return 1
	else:
		fact = 1
		#when n gearter than 1 , factorial is according to that value.
		while(n > 1):
			fact =fact * n
			n = n - 1
		return fact

# Driver Code
num= int(input("enter num:"))
print(f"Factorial of {num} is {factorial(num)}")


