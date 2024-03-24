# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.

import random
def roll_dice(num_dice=1):
    while True:
        for _ in range(num_dice):
            result = random.randint(1,6)
            print("You rolled:", result)
        choice = input("Roll again? (yes/no): ").lower()
        if choice != 'yes':
            break


if __name__ == "__main__":
    num_dice = 1
    roll_input = input("how many dice would you like to roll? (default is 1): ")
    if roll_input.isdigit():
        num_dice = int(roll_input)
    roll_dice(num_dice)