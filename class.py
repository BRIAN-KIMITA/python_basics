class students:
    def __init__(self,name,course,gender,age):
        self.name=name
        self.course = course
        self.gender = gender
        self.age = age

    def wanafunzi(self):
       print("name: %s \ncourse: %s \ngender: %s \nage: %s"
           % (self.name,self.course,self.gender,self.gender))
student1=students("brian","mathematics","male",23)
student2=students("eric","computer science","male",78)
student3=students("irene","IT","female",29)
student4=students("mucheru","psychology","female",25)
student1.wanafunzi()
student2.wanafunzi()
student3.wanafunzi()
student4.wanafunzi()