from prettytable import PrettyTable


class RiskAssessment:
    def __init__(self, damage, reproducibility, exploitability, affected_users, discoverability):
        self.damage = damage
        self.reproducibility = reproducibility
        self.exploitability = exploitability
        self.affected_users = affected_users
        self.discoverability = discoverability

    def calculate_dread_risk(self):
        risk_value = (self.damage + self.affected_users) * (self.reproducibility + self.exploitability + self.discoverability)
        return min(risk_value, 54)

    def determine_risk_level(self, risk_value):
        if 1 <= risk_value <= 12:
            return "Notice"
        elif 13 <= risk_value <= 18:
            return "Low"
        elif 19 <= risk_value <= 36:
            return "Medium"
        elif 37 <= risk_value <= 54:
            return "High"
        else:
            return "Very High (Risk Value capped at 54)"

    def assess_risk(self):
        if 0 <= self.damage <= 10 and 0 <= self.reproducibility <= 10 and 0 <= self.exploitability <= 10 and 0 <= self.discoverability <= 10:
            risk_value = self.calculate_dread_risk()
            risk_level = self.determine_risk_level(risk_value)

            self.display_results(risk_value, risk_level)
            if risk_level == "High":
                self.take_actions_for_high_risk()

        else:
            print("Input values must be in the range 0-10.")

    def display_results(self, risk_value, risk_level):
        table = PrettyTable()
        table.field_names = ["Parameter", "Value"]
        table.add_row(["Damage", self.damage])
        table.add_row(["Reproducibility", self.reproducibility])
        table.add_row(["Exploitability", self.exploitability])
        table.add_row(["Affected Users", self.affected_users])
        table.add_row(["Discoverability", self.discoverability])
        table.add_row(["DREAD Risk Value", risk_value])
        table.add_row(["Risk Level", risk_level])

        print("Risk Assessment Results:")
        print(table)

    def take_actions_for_high_risk(self):
        print("Actions to Consider for High-Risk Issues:")
        print("- Implement immediate mitigation measures.")
        print("- Allocate necessary resources to address the issue.")
        print("- Conduct a thorough security review")


def main():
    damage = float(input("Damage (0-10): "))
    reproducibility = float(input("Reproducibility (0-10): "))
    exploitability = float(input("Exploitability (0-10): "))
    affected_users = float(input("Affected users: "))
    discoverability = float(input("Discoverability (0-10): "))

    assessment = RiskAssessment(damage, reproducibility, exploitability, affected_users, discoverability)
    assessment.assess_risk()

if __name__ == "__main__":
    main()
