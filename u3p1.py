class student :

    def __init__(self,name,rollno,sem):
        self.name=name
        self.rollno=rollno
        self.sem=sem
    
    def display(self):
        print("student name",self.name)
        print("student roll no",self.rollno)
        print("student sem",self.sem)

s1=student("meet",184,3)

s1.display()