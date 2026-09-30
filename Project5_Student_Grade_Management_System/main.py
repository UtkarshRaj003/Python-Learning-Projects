student_records = {}


# FUNCTION 1: Sirf Data Add aur Calculate karne ke liye
def add_student_data():
    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Student name cannot be empty!")
        return None  # None return karenge taaki menu ko pata chale ki data add nahi hua

    subjects = ["Python", "Maths", "English", "Computer", "Database"]
    input_marks = {}

    print("\nEnter Marks: ")
    print("")
    for subject in subjects:
        while True:
            try:
                marks = int(input(f"{subject}: "))
                if 0 <= marks <= 100:
                    input_marks[subject] = marks
                    break
                else:
                    print("Marks should be between 0 to 100.")
            except ValueError:
                print("Invalid input! Please enter an integer number.")

    # Background Calculations
    total_marks = sum(input_marks.values())
    max_marks = len(input_marks) * 100
    percentage = (total_marks / max_marks) * 100
    result = ""
    grade = ""

    high_sub, high_score = max(input_marks.items(), key=lambda item: item[1])
    low_sub, low_score = min(input_marks.items(), key=lambda item: item[1])

    highest_score = f"{high_sub} ({high_score})"
    lowest_score = f"{low_sub} ({low_score})"

    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    if percentage >= 90:
        grade = "O"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"

    # Main Dictionary mein data save karna
    student_records[student_name] = {
        "marks": input_marks,
        "total": f"{total_marks}/{max_marks}",
        "percentage": percentage,
        "grade": grade,
        "result": result,
        "highest": highest_score,
        "lowest": lowest_score,
    }

    print(f"\nSuccessfully added marks for {student_name}!\n")
    return student_name  # Naam return kar rahe hain taaki isko turant display function mein bhej sakein


# FUNCTION 2: Sirf Data Display karne ke liye
def display_student_result(student_name):
    # Check ki student records mein hai ya nahi
    if student_name not in student_records:
        print(f"\nError: Student '{student_name}' not found in records!")
        return

    # Dictionary se data extract karna
    data = student_records[student_name]
    input_marks = data["marks"]

    print("================================")
    print("        STUDENT RESULT")
    print("================================\n")

    print(f"Student: {student_name}\n")

    # Yahan alignment thoda clean kar diya hai taaki `:` ek line mein aaye
    for sub, score in input_marks.items():
        print(f"{sub:<12}: {score}")

    print("--------------------------------\n")

    print(f"{'Total':<12}: {data['total']}")
    print(f"{'Percentage':<12}: {data['percentage']:.2f}%")
    print(f"{'Grade':<12}: {data['grade']}")
    print(f"{'Result':<12}: {data['result']}")

    print("--------------------------------\n")

    print(f"{'Highest':<12}: {data['highest']}")
    print(f"{'Lowest':<12}: {data['lowest']}")
    print("================================")


def display_batch_report():
    print("============================================================")
    print("                  FINAL BATCH REPORT")
    print("============================================================")
    # print("Roll/ID    Name        Total     Percentage    Result")
    print(f"{'Roll/ID':<10}{'Name':<18}{'Total':<10}{'Percentage':<14}{'Result'}")
    print("------------------------------------------------------------")

    passed_count = 0
    failed_count = 0
    top_student = ""
    highest_percentage = -1

    roll_id = 1

    for name, data in student_records.items():
        total_str = data["total"].split("/")[0]
        pct_val = data["percentage"]
        res_val = data["result"]

        pct_display = f"{pct_val:.2f}%"

        print(f"{roll_id:<10}{name:<18}{total_str:<10}{pct_display:<14}{res_val}")

        if res_val == "PASS":
            passed_count += 1
        else:
            failed_count += 1

        if pct_val > highest_percentage:
            highest_percentage = pct_val
            top_student = name

        roll_id += 1

    print("------------------------------------------------------------\n")
    print("🏆 BATCH HIGHLIGHTS:")
    print("------------------------------------------------------------")
    print(f"{'Top Student':<21}: {top_student}")
    print(f"{'Highest Percentage':<21}: {highest_percentage}")
    print(f"{'Total Passed':<21}: {passed_count}")
    print(f"{'Total Failed':<21}: {failed_count}")
    print("============================================================")


# --- Execution Control ---
# Naya data add karo aur jo naam mile usko seedhe display function mein daal do
# added_name = add_student_data()
# if added_name:
#     display_student_result(added_name)


def main():
    while True:
        print("\nMenu:")
        print("1. Add Student Data")
        print("2. Search Single Student")
        print("3. Show All Students")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student_data()
        elif choice == "2":
            search_name = input("Enter Student Name: ").strip()
            display_student_result(search_name)
        elif choice == "3":
            display_batch_report()
        elif choice == "4":
            print("\nExiting the Student Grade Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please choose a valid option (1-4).")


# Runs the program
if __name__ == "__main__":
    main()
