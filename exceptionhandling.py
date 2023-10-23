name="python expt"
for j in name:
    if (j !=0):
        print(j)

x=["python","exceptions","try and except"]
try:
     for i in range(5):
         print(f"The and element from list is {i,x[i]}")
except:
      print("index out of range")