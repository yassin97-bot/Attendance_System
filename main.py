import datetime

def print_menu():
    print("\nWelcome to Attendance System")
    print("1. Register new student")
    print("2. Sign in")
    print("3. Sign out")
    print("4. Show all attendance")
    print("5. Exit")

def student_name():
    return input("Student name: ")

def student_age():
    return input("Student age: ")

while True:
    print_menu()
    choose = int(input("Choose a number: "))

    if choose == 1:
        name = student_name()
        age = student_age()
        
        with open("students.txt", "a") as file:
            file.write("Name: " + name + " | Age: " + age + "\n")
        print("✅ Student registered\n")

    elif choose == 2:
        name = student_name()
        time = datetime.datetime.now().strftime("%H:%M:%S")
        with open("attendance.txt", "a") as file:
            file.write(name + " signed in at " + time + "\n")
        print(f"✅ {name} signed in at {time}")

    elif choose == 3:
        name = student_name()
        time = datetime.datetime.now().strftime("%H:%M:%S")
        with open("attendance.txt", "a") as file:
            file.write(name + " signed out at " + time + "\n")
        print(f"✅ {name} signed out at {time}")

    elif choose == 4:
        with open("attendance.txt", "r") as file:
            content = file.read()
            print("\n📌 Attendance Records:")
            print(content)
    
    elif choose == 5:
        print("👋 Goodbye!")
        break
    
    else:
        print("❌ Invalid choice! Try again")