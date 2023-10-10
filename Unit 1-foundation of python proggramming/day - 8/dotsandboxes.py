name = input("Enter your name here: ")
print(f"{name}")
opponents_name1 = "ishaan"
opponents_name2 = "kamea"
opponents_name3 = "ketan"
opponents_name4 = "Abe"
opponents_name5 = "Alex"

round1 = int(input("Input your round one points here: "))
round2 = int(input("Input your round two points here: "))
round3 = int(input("Input your round three points here: "))
round4 = int(input("Input your round four points here: "))

round5 = int(input("Input your round five points here: "))
opp1 = int(input("Input opponents round one points here: "))
opp2 = int(input("Input opponents round two points here: "))
opp3 = int(input("Input opponents round three points here: "))
opp4 = int(input("Input opponents round four points here: "))
opp5 = int(input("Input opponents round five points here: "))

your_total = int(input("Enter total here: "))
opponents_total = int(input("Enter opponents total here: "))
tbp = your_total / 178 * 100

bp = int(round1 / 36 * 100)
bp2 = int(round2 / 36 * 100)
bp3 = int(round3 / 36 * 100)
bp4 = int(round4 / 36 * 100)
bp5 = int(round5 / 36 * 100)
 
print(" ")

print (f"{name}'s results: ")

print(" ")

print("Game #1: ")
print(f"Opponents Name: {opponents_name1}")
print(f"Your points: {round1} ")
print(f"Opponents Points: {opp1} ")
print(f"Who won game 1:{opponents_name1}")

print(" ")

print("Game #2: ")
print(f"Opponents Name: {opponents_name2}")
print(f"Your points: {round2} ")
print(f"Opponents Points: {opp2} ")
print(f"Who won game 2: {name} ")

print(" ")

print("Game #3: ")
print(f"Opponents Name: {opponents_name3}")
print(f"Your points: {round3} ")
print(f"Opponents Points: {opp3} ")
print(f"Who won game 3: {opponents_name3}")

print(" ")

print("Game #4: ")
print(f"Opponents Name: {opponents_name4}")
print(f"Your points: {round4}  ")
print(f"Opponents Points: {opp4}  ")
print(f"Who won game 4: {name} ")

print("Game #5:")
print(f"opponants name: {opponents_name5}")
print(f"your points: {round5} ")
print(f"opponents points: {opp5}")
print("who won game 5: Tie ")

print("Dots and Boxes Table Tracker:")
print(" ")
print(f"Player Name: {name}")
print("Opponent         Your Points          Opponents Points                    box % ")
print("===============================================================================")
print(f"{opponents_name1} {round1:>15} {opp1:>26} {bp:>27.2f}")
print(f"{opponents_name2} {round2:>16} {opp2:>26} {bp2:>27.2f}")
print(f"{opponents_name3} {round3:>16} {opp3:>26} {bp3:>27.2f}")
print(f"{opponents_name4} {round4:>18} {opp4:>26} {bp4:>27.2f}")
print(f"{opponents_name5} {round5:>17} {opp5:>26} {bp5:>27.2f}")
print("===============================================================================")

print(" ")

print(f"Your Total Points: {your_total}")
print(f"Total Opponent Points: {opponents_total}")
print(f"your total box percentage:{tbp :.2f}")

