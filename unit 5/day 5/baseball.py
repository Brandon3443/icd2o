# Function to read data from file
def read_baseball_data(file_path):
    names, hits, runs, rbis = [], [], [], []
    try:
        with open(file_path, "r") as file:
            # Skip the header line
            next(file)
            for line in file:
                data = line.strip().split(',')
                names.append(data[0])
                hits.append(int(data[1]))
                runs.append(int(data[2]))
                rbis.append(int(data[3]))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return names, hits, runs, rbis

# Function to display all baseball player statistics
def display_all_baseball_stats(names, hits, runs, rbis):
    for index in range(len(names)):
        print(f"|{names[index]:<25}|{hits[index]:>6}|{runs[index]:>6}|{rbis[index]:>6}|")

# Function to calculate and display average baseball statistics
def calculate_and_display_average(hits, runs, rbis):
    if not hits or not runs or not rbis:
        print("No data available for calculation.")
        return
 
    average_hits = sum(hits) / len(hits)
    average_runs = sum(runs) / len(runs)
    average_rbis = sum(rbis) / len(rbis)
 
    print(f"Average Hits: {average_hits:.2f}")
    print(f"Average Runs: {average_runs:.2f}")
    print(f"Average RBIs: {average_rbis:.2f}")
# Function to identify the baseball player with the highest stats in a category
def stat_leader(category):
    maxIndex = 0
    for Index in range(len(names)):
        if category == "Hits":
            if hits[maxIndex] < hits[Index]:
                maxIndex = Index
        elif category == "RBIs":
             if rbis[maxIndex] < rbis[Index]:
                maxIndex = Index
        
    if category == "Hits":
        print(f"the player withe most Hits is {names[maxIndex]} with {hits[maxIndex]}")
    elif category == "RBIs":
        print(f"the player withe most RBIs is {names[maxIndex]} with {rbis[maxIndex]}")

# Function to display the top 10 players in a specified category
def display_top_10_in_category(names, hits, runs, rbis, category):
    categories = {
        "Hits": hits,
        "Runs": runs,
        "RBIs": rbis}
    if category not in categories:
        print("Invalid category. Please choose from Hits, Runs, or RBIs.")
        return
    data = categories[category]
    sorted_indices = sorted(range(len(data)), key=lambda i: data[i], reverse=True)
    print(f"Top 10 Players in {category}:")
    for i in range(min(10, len(data))):
        print(f"{i + 1}. {names[sorted_indices[i]]}: {data[sorted_indices[i]]}")
player_names = ["Cheryl Townsend", "Christina Leon", "Cassandra Ward PhD", ...]  # Replace with the actual names
hits_data = [260, 35, 329, ...]  # Replace with the actual Hits data
runs_data = [64, 118, 56, ...]  # Replace with the actual Runs data
rbis_data = [72, 18, 11, ...]  # Replace with the actual RBIs data
display_top_10_in_category(player_names, hits_data, runs_data, rbis_data, "Hits")
display_top_10_in_category(player_names, hits_data, runs_data, rbis_data, "Runs")
display_top_10_in_category(player_names, hits_data, runs_data, rbis_data, "RBIs")
def add_new_player(names, hits, runs, rbis):
    name = str(input("Enter the player's name: "))
    hit = int(input("Enter the number of hits: "))
    run = int(input("Enter the number of runs: "))
    rbi = int(input("Enter the number of RBIs: "))

    names.append(name)
    hits.append(hit)
    runs.append(run)
    rbis.append(rbi)
# Main program
if __name__ == "__main__":
    # Specify the file path
    file_path = "baseball_stats.txt"

    # Read baseball data from the file
    names, hits, runs, rbis = read_baseball_data(file_path)

    # Display menu and handle user choices
    while True:
        print("\nMenu:")
        print("1. Display all baseball player statistics")
        print("2. Calculate and display average baseball statistics")
        print("3. Identify player with the most hits")
        print("4. Identify player with the most RBIs")
        print("5. Display top 10 players in a category")
        print("6. Add a new baseball player")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            display_all_baseball_stats(names, hits, runs, rbis)
        elif choice == "2":
            calculate_and_display_average(hits, runs, rbis)
        elif choice == "3":
            stat_leader('Hits')
        elif choice == "4":
            stat_leader('RBIs')
        elif choice == "5":
            category = input("Enter the category to display top 10 players: ")
            display_top_10_in_category(hits, runs, rbis)
        elif choice == "6":
            add_new_player(names, hits, runs, rbis)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")