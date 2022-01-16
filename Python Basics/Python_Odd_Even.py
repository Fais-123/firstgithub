age=input("enter age :")

if age>="18":
    print("You age is fine for cnic")
    cnic_status=input("enter :")
    if cnic_status=="y":
        print("eligible for cnic status")
    else:
        print("you have no cnic status")
else:
    print("you age is below ")
