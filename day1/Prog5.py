runP1 = int(input("Enter the total of player 1 in 60 balls: "))
runP2 = int(input("Enter the total of player 2 in 60 balls: "))
runP3 = int(input("Enter the total of player 3 in 60 balls: "))
strikerate1 = runP1 * 100 / 60
strikerate2 = runP2 * 100 / 60
strikerate3 = runP3 * 100 / 60
print("Strike rate of player 1 is", strikerate1)
print("Strike rate of player 2 is", strikerate2)
print("Strike rate of player 3 is", strikerate3)
print("Runs scored by player 1 if they played 60 more balls is", runP1 * 2)
print("Runs scored by player 2 if they played 60 more balls is", runP2 * 2)
print("Runs scored by player 3 if they played 60 more balls is", runP3 * 2)
print("Maximum number of sixes player 1 could hit =", runP1 // 6)
print("Maximum number of sixes player 2 could hit =", runP2 // 6)
print("Maximum number of sixes player 3 could hit =", runP3 // 6)
