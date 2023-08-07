#!/usr/bin/python3

amount = float(input("Give the amount in euros: "))
# Calculate the number of 2 Euro coins
2Euro_coins = int(amount / 2)

# Calculate the number of 1 Euro coins
1Euro_coins = int((amount - 2Euro_coins * 2))

# Calculate the number of 50c Euro coins
fifty_cent_coins = int((amount - 2Euro_coins * 2 - 1euro_coins * 1) / 0.50)

# Calculate the remainder
remainder= amount - 2Euro_coins * 2 - 1euro_coins * 1 - fifty_cent_euro_coins * 0.50

# Print the results on the screen
print(amount, "can split into:", 2Euro_coins, "of 2 Euro coins,", 1euro_coins, "of 1 Euro Coins,", fifty_cent_euro_coins, "of 50 cent Euro coins with remainder:", remainder)
