from prettytable import PrettyTable

class RiskAssessmentTool:
    @staticmethod
    def calculate_dread_risk(damage, reproducibility, exploitability, affected_users, discoverability):
        risk_value = (damage + affected_users) * (reproducibility + exploitability + discoverability)
        return risk_value

    @staticmethod
    def determine_risk_level(risk_value):
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

    def assess_risk(self, damage, reproducibility, exploitability, affected_users, discoverability):
        if 0 <= damage <= 10 and 0 <= reproducibility <= 10 and 0 <= exploitability <= 10 and 0 <= discoverability <= 10:
            risk_value = self.calculate_dread_risk(damage, reproducibility, exploitability, affected_users, discoverability)

            # Cap the risk value at 54 if it exceeds that value
            risk_value = min(risk_value, 54)

            risk_level = self.determine_risk_level(risk_value)

            table = PrettyTable()
            table.field_names = ["Parameter", "Value"]
            table.add_row(["Damage", damage])
            table.add_row(["Reproducibility", reproducibility])
            table.add_row(["Exploitability", exploitability])
            table.add_row(["Affected Users", affected_users])
            table.add_row(["Discoverability", discoverability])
            table.add_row(["DREAD Risk Value", risk_value])
            table.add_row(["Risk Level", risk_level])

            print("Risk Assessment Results:")
            print(table)

            if risk_level == "High":
                print("Actions to Consider for High-Risk Issues:")
                print("- Implement immediate mitigation measures.")
                print("- Allocate necessary resources to address the issue.")
                print("- Conduct a thorough security review.")
        else:
            print("Input values must be in the range 0-10.")

if __name__ == "__main__":
    risk_tool = RiskAssessmentTool()
    
    damage = float(input("Damage (0-10): "))
    reproducibility = float(input("Reproducibility (0-10): "))
    exploitability = float(input("Exploitability (0-10): "))
    affected_users = float(input("Affected users: "))
    discoverability = float(input("Discoverability (0-10): "))
    
    risk_tool.assess_risk(damage, reproducibility, exploitability, affected_users, discoverability)
