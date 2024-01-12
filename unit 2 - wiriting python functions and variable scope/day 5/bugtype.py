def input_bug_count(bug_type):
    count = int(input(f"Enter the count of {bug_type} bugs: "))
    return count


def calculate_percent(total, count):
    percent = (count / total) * 100
    return percent


def input_bug_type_and_count():
    bug_type = input("Enter the type of bug: ")
    count = input_bug_count(bug_type)
    return bug_type, count


def display_table(bug1, count1, bug2, count2, bug3, count3):
    total = count1 + count2 + count3
    print("Bug Type     Count   Percentage")
    print("---------------------------------")
    print(f"{bug1}{count1:>15}{calculate_percent(total, count1):>12f}%")
    print(f"{bug2}{count2:>15}{calculate_percent(total, count2):>12f}%")
    print(f"{bug3}{count3:>15}{calculate_percent(total, count3):>12f}%")
    print("---------------------------------")
    print("Bug Type      Count       100% ")

bug1_type, bug1_count = input_bug_type_and_count()
bug2_type, bug2_count = input_bug_type_and_count()
bug3_type, bug3_count = input_bug_type_and_count()

display_table(bug1_type, bug1_count, bug2_type, bug2_count, bug3_type, bug3_count)