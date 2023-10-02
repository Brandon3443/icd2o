# Define data
item1 = "Apples"
quantity1 = 12
price1 = 0.75

item2 = "Dragon Fruit"
quantity2 = 20
price2 = 0.60

item3 = "Cherries"
quantity3 = 8
price3 = 2.50

item4 = "Dates"
quantity4 = 15
price4 = 1.20

# Print table
print(f"{'Item':<10} {'Quantity':>10} {'Price ($)':>10}")
print(f"{item1:<10} {quantity1:>10} {price1:>10.2f}")
print(f"{item2:<10.10} {quantity2:>10} {price2:>10.2f}")  #Dragon Fruit is more than 10 so we truncated at 10
print(f"{item3:<10} {quantity3:>10} {price3:>10.2f}")
print(f"{item4:<10} {quantity4:>10} {price4:>10.2f}")