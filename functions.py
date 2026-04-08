import random
import math
from datetime import datetime, timedelta


def generate_marks():
    marks = [random.randint(50, 100) for _ in range(5)]
    print("Student Marks:", marks)

    print("Highest:", max(marks))
    print("Lowest:", min(marks))


def password_generator():
    chars = "abc123XYZ@#"
    password = "".join(random.choice(chars) for _ in range(6))
    print("Generated Password:", password)



def date_calculator():
    today = datetime.now()
    exam_date = today + timedelta(days=10)

    print("Today:", today.strftime("%d-%m-%Y"))
    print("Exam Date (after 10 days):", exam_date.strftime("%d-%m-%Y"))



def math_demo():
    num = 25
    print("Square root:", math.sqrt(num))
    print("Power (3^3):", math.pow(3, 3))
    print("Ceil of 4.2:", math.ceil(4.2))


if __name__ == "__main__":
    print("---- MODULES TASK ----\n")
    generate_marks()
    print()
    password_generator()
    print()
    date_calculator()
    print()
    math_demo()