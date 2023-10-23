num=int(input("Enter a number: "))
if num>0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number")
age=int(input("Enter Eligible age to vote: "))
if age>18 and age<=81:
    print("The person is eligible to vote")
else:
    print("Not eligible to vote/you have exceeded voting age")
#marks and grade scored
marks=int(input("Enter Marks Scored "))
if marks>=70 and marks<=100:
    print("You have scored an A")
elif marks>=60 and marks <=69:
    print("You have scored an B")
elif marks>=50 and marks <=59:
    print("You have scored an C")
elif marks>=40 and marks <=49:
    print("You have scored an D")
else:
    print("you have failed")
