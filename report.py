def ask_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    img_path = input("Enter image path: ")
    return name, age, img_path

def line():
    print("-" * 50)
