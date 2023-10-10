import os
import time
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_terminal(elements, dice_results):
    clear_screen()
    print("╔════════════════════╗")
    print("║  Forest Adventure  ║")
    print("╠════════════════════╣")
    for element in elements:
        print(f"║  {element}")
    print("╠════════════════════╣")
    print("║  Enter a command:  ║")
    print("║  'read', 'wait',   ║")
    print("║  'interact', or    ║")
    print("║  'roll' for dice   ║")
    print("╠════════════════════╣")
    print("║  Dice Results:     ║")
    for die, result in dice_results.items():
        print(f"║  {die}: {result:2}       ║")
    print("╚════════════════════╝")

def main():
    elements = []
    scenario_shown = False
    story_step = 0
    waits = 0

    story_texts = [
        "You find yourself in a mysterious forest...",
        "You see a strange book lying on the ground.",
        "The forest is silent, and time seems to stand still.",
        "You notice a hidden path through the trees.",
        "A friendly squirrel approaches you and chatters away.",
        "There's nothing more to do here.",
    ]

    # Create an instance of the DiceRoller class
    dice_roller = DiceRoller()

    while True:
        if not scenario_shown:
            elements.append(story_texts[story_step])
            scenario_shown = True
        render_terminal(elements, dice_roller.get_results())

        command = input("\nEnter a command (type 'exit' to quit): ").lower()
        if command == 'exit':
            break
        elif command == 'read':
            if story_step < len(story_texts) - 1:
                story_step += 1
                elements.append(f'You read and the story advances: {story_texts[story_step]}')
            else:
                elements.append("You've reached the end of the story.")
        elif command == 'interact':
            if story_step == 4:
                elements.append("You interact with the friendly squirrel, and it leads you to a hidden treasure!")
            elif story_step == 5:
                elements.append("The creature challenges you to a battle. You must roll")
            else:
                elements.append("You chose to interact, but nothing special happens.")
        elif command == 'wait':
            waits += 1
            if waits == 1:
                elements.append("You wait for a few minutes.")
            elif waits == 2:
                elements.append("You wait for a few hours.")
            elif waits == 3:
                elements.append("You wait for several days, and a mysterious creature appears!")
                # Handle the event for the third wait (e.g., interaction with the creature).
            else:
                elements.append("You've waited enough, you leave the forest")
        elif command == 'roll':
            dice_roller.roll_all_dice()
        else:
            elements.append("Invalid command. Please enter 'read', 'wait', 'interact', or 'roll' for dice.")

if __name__ == "__main__":
    main()
