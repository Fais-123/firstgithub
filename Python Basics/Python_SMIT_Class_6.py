####
a=int(input("enter num:"))
b=int(input("enter num:"))
c=int(input("enter num:"))
d=int(input("enter num:"))

if a==b:
    print("a and b are equal")
    if b==c:
        print("b and c are equal")
        if c==d:
             print("äll are equal")
        else:
             print("äll are not equal")
    else:
        print("b and c are not equal")
else:
      print("a and b are not equal")
#####
age=input("enter age :")

if age>="18":
    print("You are eligible")
    cnic_status=input("enter :")

    if cnic_status=="y":
        print("eligible for cnic")
    else:
        print("you have no cnic status")
else:
    print("you are not eligible")

