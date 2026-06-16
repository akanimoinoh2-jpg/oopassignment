class Futurelabs:
    def __init__(self, name,skill):
        self.name=name
        self.skill=skill

    def registration(self):
        print(f"{self.name} is a student of future labs, is in {self.skill} department") 

class student2 (Futurelabs):
    def __init__(self, name,skill,age):
        self.name=name
        self.skill=skill
        self.age=age

    def performance(self):
        print(f"{self.name} performance is excellent in {self.skill}")

class student3(Futurelabs):
    def __init__(self, name, skill,grade):
        self.name=name
        self.skill=skill
        self.grade=grade

    def remark(self):
        print(f"s{self.name} is excellent(A1).") 

#creating object
Futurelabs1= Futurelabs("John", "backend") 
student2= student2 ("Daniel", "Frontend development",20) 
student3= student3("Samuel","Programming","A1") 

Futurelabs1.registration()
student2.performance()
student3.remark()



print(Futurelabs1.name)
print(Futurelabs1.skill)

print()

print(student2.name)
print(student2.skill)
print(student2.age)

print()

print(student3.name)
print(student3.skill)
print(student3.grade)





    





        