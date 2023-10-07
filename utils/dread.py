from prettytable import PrettyTable
from calc import run_risk_calculator


class RiskAssessment:
    DREAD_RISK_CAP = 54
    RISK_LEVELS = {
        (1, 12): "Notice",
        (13, 18): "Low",
        (19, 36): "Medium",
        (37, DREAD_RISK_CAP): "High",
    }

    def __init__(self, damage, reproducibility, exploitability, affected_users, discoverability):
        self.damage = damage
        self.reproducibility = reproducibility
        self.exploitability = exploitability
        self.affected_users = affected_users
        self.discoverability = discoverability
        self.results = {}  # Dictionary to store results

    def calculate_dread_risk(self):
        risk_value = (self.damage + self.affected_users) * (self.reproducibility + self.exploitability + self.discoverability)
        return min(risk_value, self.DREAD_RISK_CAP)

    def determine_risk_level(self, risk_value):
        for (min_range, max_range), level in self.RISK_LEVELS.items():
            if min_range <= risk_value <= max_range:
                return level
        return "Very High (Risk Value capped at {})".format(self.DREAD_RISK_CAP)

    def assess_risk(self):
        if 0 <= self.damage <= 10 and 0 <= self.reproducibility <= 10 and 0 <= self.exploitability <= 10 and 0 <= self.discoverability <= 10:
            risk_value = self.calculate_dread_risk()
            risk_level = self.determine_risk_level(risk_value)
            self.results["Risk Value"] = risk_value
            self.results["Risk Level"] = risk_level
            if risk_level == "High":
                self.results["High Risk Actions"] = self.take_actions_for_high_risk()
            return True
        else:
            print("Input values must be in the range 0-10.")
            return False

    def display_results(self):
        table = PrettyTable()
        table.field_names = ["Parameter", "Value"]
        table.add_row(["Damage", self.damage])
        table.add_row(["Reproducibility", self.reproducibility])
        table.add_row(["Exploitability", self.exploitability])
        table.add_row(["Affected Users", self.affected_users])
        table.add_row(["Discoverability", self.discoverability])
        for key, value in self.results.items():
            table.add_row([key, value])

        print("Risk Assessment Results:")
        print(table)

    def take_actions_for_high_risk(self):
        return ["Implement immediate mitigation measures.", "Allocate necessary resources to address the issue.", "Conduct a thorough security review"]
def main():
    try:
        damage = float(input("Damage (0-10): "))
        reproducibility = float(input("Reproducibility (0-10): "))
        exploitability = float(input("Exploitability (0-10): "))
        affected_users = float(input("Affected users: "))
        discoverability = float(input("Discoverability (0-10): "))

        assessment = RiskAssessment(damage, reproducibility, exploitability, affected_users, discoverability)
        if assessment.assess_risk():
            name = input("Enter a name to save this assessment: ")
            assessments[name] = assessment.results
            assessment.display_results()

            # Ask if the user wants to run the risk calculator
            run_calculator = input("Do you want to run the risk calculator? (yes/no): ")
            if run_calculator.lower() == "yes":
                run_risk_calculator()

    except ValueError:
        print("Invalid input. Please enter numeric values in the specified range.")

if __name__ == "__main__":
    assessments = {}  # Dictionary to store assessments
    main()