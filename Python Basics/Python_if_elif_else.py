#Take student roll no and print his result.
roll_no=int(input("enter roll number:"))

#Take marks of each subject, calculate percentage and grade that.

english=int(input("enter eng marks:"))
maths=int(input("enter maths marks:"))
sst=int(input("enter sst marks:"))
sci=int(input("enter sci marks:"))
urdu=int(input("enter urdu marks:"))

obtain_marks=english+maths+sst+sci+urdu
print(obtain_marks)
total_marks=int(input("enter total marks:"))
percentage=obtain_marks * 100/ total_marks
print(percentage)

#percentage=float(input("Enter Percentage :"))
if percentage>=90:
    print("A*")
elif percentage>=80:
    print("A+")
elif percentage>=70:
    print("A")
elif percentage>=60:
    print("B")
elif percentage>=50:
    print("C")
else:
    print("ungraded")
