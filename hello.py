def add_student():
    with open("students.txt", "a") as file:
        print("Enter the detail of student")
        name = input("Enter the name :")
        roll_no = input("Enter the roll_no.")

        m1=input("Enter subject 1 marks :")
        m2=input("Enter subject 2 marks :")
        m3=input("Enter subject 3 marks :")

        total = m1+m2+m3
        file.write(
            f"Name: {name}, Roll No: {roll_no}, "
            f"Subject 1: {m1}, Subject 2: {m2}, Subject 3: {m3}\n "
             
        )

def view_student():
    with open("stdent","r") as file:
        print(file.read())

def search():
    search_roll = input("Enter Roll Number to search: ")
    found = False

    with open("students.txt", "r") as file:
        for line in file:
            
            if f"Roll No: {search_roll}," in line:
                print(line.strip())
                found = True
                break

    if not found:
        print(f"No student found with Roll Number: {search_roll}")

def calculate_average(students):
    print("\n--- Calculate Average Marks ---")
    roll = input("Enter roll number: ").strip()

    for student in students:
        if student[0] == roll:
            marks = student[2]
            total = sum(marks)
            avg = total / len(marks)
            print("Student Name:", student[1])
            print("Average Marks:", round(avg, 2))
            return

    print("Student not found.")

def main():
    

    while True:
        print("\n--- Student Record Menu ---")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by roll number")
        print("4. Calculate average marks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")

main()
