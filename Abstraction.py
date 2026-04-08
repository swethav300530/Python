class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def result(self):
        self.__calculate_grade()

 
    def __calculate_grade(self):
        if self.marks >= 90:
            grade = "A"
        elif self.marks >= 75:
            grade = "B"
        elif self.marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", grade)
        print()



s1 = Student("Swetha", 95)
s2 = Student("Arun", 70)
s3 = Student("Kavi", 40)

s1.result()
s2.result()
s3.result()