# result1 = str(input("Input whether you won or lost game 1: "))
# result2 = str(input("Input whether you won or lost game 2: "))
# result3 = str(input("Input whether you won or lost game 3: "))
# result4 = str(input("Input whether you won or lost game 4: "))
# result5 = str(input("Input whether you won or lost game 5: "))
# result6 = str(input("Input whether you won or lost game 6: "))

# wins = 0

# if result1 == "W":
#     wins += 1
# if result2 == "W":
#     wins += 1
# if result3 == "W":
#     wins += 1
# if result4 == "W":
#     wins += 1
# if result5 == "W":
#     wins += 1
# if result6 == "W":
#     wins += 1

# if wins == 5 or wins == 6:
#     print("1")
# elif wins == 3 or wins == 4:
#     print("2")
# elif wins == 1 or wins == 2:
#     print("3")
# else:
#     print("-1")



grid = []
for _ in range(4):
    grid.append(list(map(int, input().split())))

l_sum = sum(grid[0])
for line in grid[1:] + list(zip(*grid)):
    if sum(line) != l_sum:
        print("not magic")
        break
else:
    print("magic")