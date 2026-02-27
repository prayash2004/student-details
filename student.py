students = []

while True:
    print("\n===== Welcome =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Result")
    print("5. Exit")
    print("6. Update Marks")
    print("7. Show Topper")
    print("8. Count Students")
    print("9. Sort by Total Marks")
    print("10. Class Average")
    print("11. Pass/Fail List")
    print("12. Student Grade")
    print("13. Clear All Records")
    print("14. Exit")

    choice = input("Enter choice: ")

    # Add Student
    if choice == "1":
        name = input("Name: ")
        roll = input("Roll: ")
        m1 = int(input("Marks 1: "))
        m2 = int(input("Marks 2: "))
        m3 = int(input("Marks 3: "))
        students.append([name, roll, m1, m2, m3])
        print("Student added!")

    # Show Students
    elif choice == "2":
        for s in students:
            print(s)

    # Search Student
    elif choice == "3":
        r = input("Enter roll: ")
        for s in students:
            if s[1] == r:
                print("Found:", s)

    # Result
    elif choice == "4":
        for s in students:
            total = s[2]+s[3]+s[4]
            avg = total/3

            if avg >= 90:
                grade = "A"
            elif avg >= 75:
                grade = "B"
            elif avg >= 50:
                grade = "C"
            else:
                grade = "Fail"

            print(s[0], "Total:", total, "Avg:", avg, "Grade:", grade)

    # Exit
    elif choice == "5":
        print("Bye")
        break

    # Update Marks
    elif choice == "6":
        r = input("Enter roll: ")
        for s in students:
            if s[1] == r:
                s[2] = int(input("New Marks1: "))
                s[3] = int(input("New Marks2: "))
                s[4] = int(input("New Marks3: "))
                print("Updated!")

    # Show Topper
    elif choice == "7":
        topper = max(students, key=lambda s: s[2]+s[3]+s[4])
        print("Topper:", topper)

    # Count Students
    elif choice == "8":
        print("Total Students:", len(students))

     #9 Sort by Total Marks
    elif choice == "9":
        students.sort(key=lambda s: s[2]+s[3]+s[4], reverse=True)
        for s in students:
            print(s)

    # 10 Class Average
    elif choice == "10":
        if students:
            total = sum(s[2]+s[3]+s[4] for s in students)
            print("Class Average:", total/(3*len(students)))
        else:
            print("No data")

    # 11 Pass/Fail List
    elif choice == "11":
        for s in students:
            avg = (s[2]+s[3]+s[4])/3
            print(s[0], "Pass" if avg>=50 else "Fail")

    # 12 Student Grade
    elif choice == "12":
        r = input("Enter roll: ")
        for s in students:
            if s[1] == r:
                avg = (s[2]+s[3]+s[4])/3
                if avg>=90: g="A"
                elif avg>=75: g="B"
                elif avg>=50: g="C"
                else: g="Fail"
                print("Grade:", g)

    # 13 Clear All Records
    elif choice == "13":
        students.clear()
        print("All records deleted!")

    # 14 Exit
    elif choice == "14":
        print("Program closed")
        break

    else:
        print("Invalid choice")
