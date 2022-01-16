#Python Program to find the LCM of Two Numbers 
num1=int(input("enter num:"))
num2=int(input("enter num:"))

#Assign  max  number beteen both to  variable name(greater)
if(num1>num2):
    greater=num1
else:
    greater=num2

while(True):
    if(greater%num1==0 and greater%num2==0):
        break
    greater=greater+1

print(f"The lcm of {num1} and {num2} is {greater}")
