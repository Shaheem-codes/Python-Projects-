import random

# Dice shapes stored as list of lines (important for horizontal printing)
dice_art = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ],
    2: [
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ],
    3: [
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ],
    4: [
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ],
    5: [
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ],
    6: [
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    ]
}

print(" Welcome to Dice Roller Game!")

while True:
    choice = input("\nRoll the dice? (y/n): ").lower()

    if choice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        total = dice1 + dice2

        # get both dice drawings
        d1 = dice_art[dice1]
        d2 = dice_art[dice2]

        print()

        # print line by line horizontally
        for i in range(5):
            print(d1[i], " ", d2[i])

        print(f"\n Total: {total}")

    elif choice == "n":
        print(" Thanks for playing!")
        break

    else:
        print(" Invalid input! Enter y or n only.")
