from Greeting_module import greet, welcome, bye

def show_all(*names):
    print("Names:", names)

def details(**info):
    print("Details:", info)

def display_all(*names, **info):
    print("Names:", names)
    print("Info:", info)


greet("Swetha")
welcome("Chennai")
bye("Swetha")

show_all("A", "B", "C")


