class Student:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        self.lap =self.laptop()

    def show(self):
        print(self.name,self.age)  

    class laptop():
      def __init__(self):
        self.brand = "HP"
        self.cpu = "i5"
        self.ram = 8
      def show():
        print()

s1 = Student("mansi",22)
s2 = Student("pooja",33)
lap1 = s1.laptop()
lap2 = Student.laptop()
print(lap2.brand)
print(lap1.brand)
s1.show()
s2.show()