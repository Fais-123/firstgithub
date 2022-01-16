import cmath
import math
###roots of quadratic equation
##
##a=int(input("enter a:"))
##b=int(input("enter b:"))
##c=int(input("enter c:"))
##
###formula
##d=(b**2)-(4*a*c)
##
##sol1 = (-b-cmath.sqrt(d))/(2*a)  
##sol2 = (-b+cmath.sqrt(d))/(2*a) 
##
##print(f"The roots of quadratic equation are {sol1} and {sol2}")

##functions for quadratic eq
def quad(a,b,c):
    d=b**2-4*a*c
    sol=math.sqrt(abs(d))

# checking condition for discriminant
    if(d>0):
       print(" real and different roots ")
       print((-b + sol)/(2 * a))
       print((-b - sol)/(2 * a))

    elif(d==0):
        print("real and same roots")
        print(-b/(2 * a))

    else:
        print("Complex roots")
        print(- b / (2 * a), " + i", sol) 
        print(- b / (2 * a), " - i", sol)


a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

# If a is 0, then incorrect equation  
if a == 0:  
    print("Input correct quadratic equation")  
  
else:  
    quad(a,b,c)


