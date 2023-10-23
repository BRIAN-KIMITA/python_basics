#list- variables holdinng ,multiple values
fruits=["mangoes","oranges","apples","pineapples","watermelon","bananas"]
fruits.sort()
num=[-2,4,5,1,5,3,67,8,79]
num[3]=80
rep=num*2
print(rep)
print(num.sort())
print(num)

print(len(num))
print(fruits)
print("I love eating " +fruits[1])
#tuples are immutable and orderedn
cars=("Mercedes","mazda6","Toyota")
# cars[0]="wagon" does not support assignment changes
type= cars*8
print(cars[0])
print(type.count("mazda6"))
#sets are unordered
days={"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"}
print(days)
# dictionaries
staff_details ={"name":"Brian","Age":30,"company":"Emobilis","gender":"male","salary":125000}
print(staff_details)
print(f"name: %s" %staff_details["name"])
print(f"age: %s" %staff_details["Age"])
print(f"company: %s" %staff_details["company"])
print(f"gender: %s" %staff_details["gender"])
print(f"salary: %s" %staff_details["salary"])

