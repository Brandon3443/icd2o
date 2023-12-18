import random

def get_player_input(assets):
    while True:
        try:
            lemonade_cups = int(input("Enter the number of cups of lemonade you would like to make: "))
            if lemonade_cups < 0 or lemonade_cups > 100:
                print("Number of cups must be between 0 and 100. You do not have an infinite supply. Please enter a valid number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for the number of cups.")

    while True:
        try:
            advertising_signs = int(input("Enter the number of advertising signs to buy (up to 10): "))
            if advertising_signs < 0 or advertising_signs > 10:
                print("Number of advertising signs must be between 0 and 10. Please enter a valid number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for the number of advertising signs.")

    while True:
        try:
            price_per_cup = float(input("Enter the price per cup of lemonade (in cents): "))
            if price_per_cup < 0:
                print("Sell price cannot be negative. Please enter a valid number.")
            elif price_per_cup > 50:
                print("Sell price per cup cannot exceed 50 cents. Please enter a valid number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for the sell price.")

    # Check if the player has enough assets
    cost_lemonade = lemonade_cups * 5  # Each cup costs 5 cents to make
    cost_signs = advertising_signs * 15  # Each sign costs 15 cents
    total_cost = cost_lemonade + cost_signs

    if total_cost > assets:
        print("Insufficient funds. Cannot afford to make lemonade and buy signs. Please try again.")
    else:
        # Update assets after spending money
        assets -= total_cost
        return lemonade_cups, advertising_signs, price_per_cup, assets

def simulate_day(lemonade_cups, price_per_cup, assets, weather, day_counter):
    if day_counter == 6 and random.random() < 0.13:
        print("Oh no! Ishaan pulled up and may have attacked you on day 6 and stolen all your money! You're bankrupt!")
        assets = 0
        return 0, 0, assets

    # Adjust the number of cups sold based on weather
    if weather == "sunny":
        cups_sold = max(15, lemonade_cups - 5)  # Sell between 15 and the user-inputted amount
    else:
        max_rainy_cups = max(10, lemonade_cups - 10)
        cups_sold = random.randint(10, max_rainy_cups)  # Random number from 10 to the adjusted maximum

    # Check capacity
    cups_sold = min(cups_sold, 50)

    revenue = cups_sold * min(price_per_cup, 50)  # Ensure sell price does not exceed 50 cents

    # Update assets based on revenue
    assets += revenue

    return cups_sold, revenue, assets

def display_day_costs(lemonade_cups, advertising_signs):
    print(f"\nDay Costs:")
    print(f"Cost to make a cup of lemonade: {lemonade_cups * 5} cents")
    print(f"Cost to buy an advertising sign: {advertising_signs * 15} cents")

def get_weather_intro(weather):
    if weather == "sunny":
        return "The weather is sunny. Many people are likely looking for something to cool them down."
    else:
        return "The weather is rainy. Not many people are going outside to get lemonade."

def get_weather():
    # Randomly determine the weather as either "sunny" or "rainy"
    return random.choice(["sunny", "rainy"])

def main():
    # Set initial assets
    starting_assets = 200  # $2 in cents
    # Get starting money from the player
    while True:
        try:
            print("Hi there🖐, you are now running your own lemonade stand!")
            print("You will need to make 3 decisions daily:")
            print("how many cups you make, how many advertising signs to make, and what price to set the lemonade at.")
            print("The profits are the difference between the income and your expenses.")
            print("Keep track of your assets so that you don't spend more than you have.")
            assets = int(input("Enter the amount of money to start with (between $2 and $5, enter in hundreds (100 cents = 1 dollar)): ") or starting_assets)
            if 200 <= assets <= 500:
                break
            else:
                print("Invalid amount. Please enter an amount between $2 and $5 (please enter in hundreds).")
        except ValueError:
            print("Invalid input. ENTER A PROPER NUMBER!!!")

    print(f"Your starter assets is: ${assets / 100:.2f}")

    # Initialize day counter
    day_counter = 1

    while day_counter <= 15:
        print(f"\nDay {day_counter}")

        # Get the weather for the day
        weather = get_weather()
        print(get_weather_intro(weather))

        # Get player input with validation
        lemonade_cups, advertising_signs, price_per_cup, assets = get_player_input(assets)

        # Display day costs
        display_day_costs(lemonade_cups, advertising_signs)

        # Simulate the day
        cups_sold, revenue, assets = simulate_day(lemonade_cups, price_per_cup, assets, weather, day_counter)

        # Display recap for the day
        print("\nDay Recap:")
        print(f"Cups of lemonade made: {lemonade_cups}")
        print(f"Advertising signs bought: {advertising_signs}")
        print(f"Cups sold: {cups_sold}")
        print(f"Revenue: ${revenue / 100:.2f}")  # Convert revenue back to dollars
        print(f"Current assets: ${assets / 100:.2f}")  # Convert assets back to dollars

        # Increment the day counter
        day_counter += 1

        # Ask if the player wants to continue
        user_input = input("\nDo you want to continue to the next day? (yes/no, not entering yes or no will result in an automatic game end): ").lower()
        if user_input != 'yes':
            break

    # Display final results
    print("\nGame Over! Final Results:")
    print(f"Total cash made: ${assets / 100:.2f}")
    print(f"Total cups of lemonade made: {lemonade_cups * (day_counter - 1)}")
    print(f"Total signs made: {advertising_signs * (day_counter - 1)}")
    profit_loss_percentage = ((assets - starting_assets) / starting_assets) * 100
    print(f"Profit/Loss: {profit_loss_percentage:.2f}%")
    print(f"Day reached⏱: {day_counter - 1}")

if __name__ == "__main__":
    main()