def input_bug_counts(bug_type):
    count = int(input(f"Enter the count of {bug_type} bugs: "))
    return count
 
 
def calculate_percent(total, count):
    percent = (count / total) * 100
    return percent
 
 
def input_bug_type_and_count():
    bug_type = input("Enter the type of bug: ")
    count = input_bug_counts(bug_type)
    return bug_type, count
 
 
def display_table(bug1, count1, bug2, count2, bug3, count3):
    total = count1 + count2 + count3
    print("Bug Type\tCount\tPercentage")
    print("---------------------------------")
    print(f"{bug1}\t\t{count1}\t{calculate_percent(total, count1):.2f}%")
    print(f"{bug2}\t\t{count2}\t{calculate_percent(total, count2):.2f}%")
    print(f"{bug3}\t\t{count3}\t{calculate_percent(total, count3):.2f}%")
    print("---------------------------------")
bug1_type, bug1_count = input_bug_type_and_count()
bug2_type, bug2_count = input_bug_type_and_count()
bug3_type, bug3_count = input_bug_type_and_count()
 
display_table(bug1_type, bug1_count, bug2_type, bug2_count, bug3_type, bug3_count)