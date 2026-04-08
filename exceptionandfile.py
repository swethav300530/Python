def calculate_result():
    try:
        mark = int(input("Enter your mark: "))

        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")

        if mark >= 50:
            result = "Pass"
        else:
            result = "Fail"

    except ValueError as e:
        print("Error:", e)

    else:
        print("Result:", result)

    finally:
        print("Result calculation completed\n")


def division():
    try:
        a = int(input("Enter number: "))
        b = int(input("Enter divisor: "))
        print("Answer:", a / b)

    except ZeroDivisionError:
        print("Cannot divide by zero")

    except ValueError:
        print("Enter valid numbers only")

    else:
        print("Division successful")

    finally:
        print("Operation finished\n")



def file_read():
    try:
        file = open("sample.txt", "r")
        print(file.read())

    except FileNotFoundError:
        print("File not found")

    finally:
        try:
            file.close()
        except:
            pass
        print("File handling done\n")



if __name__ == "__main__":
    print("---- EXCEPTION TASK ----\n")

    calculate_result()
    division()
    file_read()