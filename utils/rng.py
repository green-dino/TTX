import random

class DiceRoller:
    def __init__(self):
        self.results = {}

    def roll_d4_outcomes(self):
        return random.randint(1, 4)

    def roll_d6_standard(self):
        return random.randint(1, 6)

    def roll_d8_stats(self):
        return random.randint(1, 8)

    def roll_d10_attributes(self):
        return random.randint(1, 10)

    def roll_d12_hp(self):
        return random.randint(1, 12)

    def roll_d20_actions(self):
        return random.randint(1, 20)

    def roll_d30_applications(self):
        return random.randint(1, 30)

    def roll_d100_percentials(self):
        return random.randint(1, 100)

    def roll_all_dice(self):
        # Roll each type of die and store the results in the dictionary
        self.results["Outcome"] = self.roll_d4_outcomes()
        self.results["Standard"] = self.roll_d6_standard()
        self.results["Stats"] = self.roll_d8_stats()
        self.results["Attributes"] = self.roll_d10_attributes()
        self.results["HP"] = self.roll_d12_hp()
        self.results["Actions"] = self.roll_d20_actions()
        self.results["Applications"] = self.roll_d30_applications()
        self.results["Percentials"] = self.roll_d100_percentials()

    def get_results(self):
        return self.results

if __name__ == "__main__":
    # Create an instance of the DiceRoller class
    dice_roller = DiceRoller()

    # Roll all dice and get the results
    dice_roller.roll_all_dice()
    results = dice_roller.get_results()

    # Print the rolls
    for die, result in results.items():
        print(f"{die}: {result}")

    # Save the rolls to a file (optional)
    with open("dice_rolls.txt", "w") as file:
        for die, result in results.items():
            file.write(f"{die}: {result}\n")

    print("Rolls saved to dice_rolls.txt")
