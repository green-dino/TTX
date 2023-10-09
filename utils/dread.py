from prettytable import PrettyTable
import math
import numpy as np

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
        self.results = {}

    def calculate_dread_risk(self):
        damage_weight = 0.4
        reproducibility_weight = 0.3
        exploitability_weight = 0.5
        affected_users_weight = 0.01
        discoverability_weight = 0.5

        # Calculate the weighted sum of the parameters using math.prod()
        weighted_sum = math.prod([
            self.damage ** damage_weight,
            self.reproducibility ** reproducibility_weight,
            self.exploitability ** exploitability_weight,
            self.affected_users ** affected_users_weight,
            self.discoverability ** discoverability_weight
        ])
        
        # list of all values
        risk_values = []

        for _ in range(10000):  # Simulate 10,000 random combinations
            # Generate random values within the specified range
            random_damage = np.random.uniform(0, 10)
            random_reproducibility = np.random.uniform(0, 10)
            random_exploitability = np.random.uniform(0, 10)
            random_affected_users = np.random.uniform(0, 10)
            random_discoverability = np.random.uniform(0, 10)

            # Calculate the composite risk for the random combination
            random_weighted_sum = (
                random_damage ** damage_weight +
                random_reproducibility ** reproducibility_weight +
                random_exploitability ** exploitability_weight +
                random_affected_users ** affected_users_weight +
                random_discoverability ** discoverability_weight
            )

            risk_values.append(random_weighted_sum)

        # Calculate the percentile rank of the original risk value within the simulated values
        percentile = np.percentile(risk_values, (weighted_sum / len(risk_values)) * 100)

         # Scale the weighted sum logarithmically to fit within your desired range (0 to DREAD_RISK_CAP)
        scaled_risk_value = min((np.log1p(weighted_sum) / np.log1p(10)) * self.DREAD_RISK_CAP, RiskAssessment.DREAD_RISK_CAP)

        risk_value = (self.damage + self.affected_users) * (self.reproducibility + self.exploitability + self.discoverability)
        return max(0, scaled_risk_value)

    def determine_risk_level(self, risk_value):
        for (min_range, max_range), level in self.RISK_LEVELS.items():
            if min_range <= risk_value <= max_range:
                return level
        return f"Very High (Risk Value capped at {self.DREAD_RISK_CAP})"

    def assess_risk(self):
        if 0 <= self.damage <= 10 and 0 <= self.reproducibility <= 10 and 0 <= self.exploitability <= 10 and 0 <= self.discoverability <= 10:
            risk_value = self.calculate_dread_risk()
            risk_level = self.determine_risk_level(risk_value)
            self.results["Risk Value"] = risk_value
            self.results["Risk Level"] = risk_level
            if risk_level == "High":
                self.results["High Risk Actions"] = self.take_actions_for_high_risk()
            return True
        elif risk_level == "Medium":
                self.results["Medium Risk Actions"] = self.take_actions_for_medium_risk()

        else:
            print("Input values must be in the range 0-10.")
            return False

    def display_results(self):
        table = PrettyTable()
        table.field_names = ["Parameter", "Value"]
        parameter_names = ["Damage", "Reproducibility", "Exploitability", "Affected Users", "Discoverability"]
        parameter_values = [self.damage, self.reproducibility, self.exploitability, self.affected_users, self.discoverability]

        for name, value in zip(parameter_names, parameter_values):
            table.add_row([name, value])

        for key, value in self.results.items():
            table.add_row([key, value])

        print("Risk Assessment Results:")
        print(table)

    def take_actions_for_high_risk(self):
        return ["Implement immediate mitigation measures.", "Allocate necessary resources to address the issue.", "Conduct a thorough security review"]
    
    def take_actions_for_medium_risk(self):
        return ["Assess and analyze", "Identify Mitigation Strategies", "Monitor and review"]
    
    def take_actions_for_low_risk(self):
        return ["monitor closely", "Document and review", "Maintain readiness"]
    
    def run_against_random_generator(self):
        risk_values = []

        for _ in range(10000):  # Simulate 10,000 random combinations
            # Generate random values within the specified range
            random_damage = np.random.uniform(0, 10)
            random_reproducibility = np.random.uniform(0, 10)
            random_exploitability = np.random.uniform(0, 10)
            random_affected_users = np.random.uniform(0, 10)
            random_discoverability = np.random.uniform(0, 10)

            # Calculate the composite risk for the random combination
            random_weighted_sum = (
                random_damage ** 0.4 +
                random_reproducibility ** 0.3 +
                random_exploitability ** 0.5 +
                random_affected_users ** 0.01 +
                random_discoverability ** 0.5
            )

            risk_values.append(random_weighted_sum)

        # Calculate the percentile rank of the original risk value within the simulated values
        percentile = np.percentile(risk_values, (self.calculate_dread_risk() / len(risk_values)) * 100)

        # Scale the percentile value to fit within your desired range (0 to DREAD_RISK_CAP)
        scaled_risk_value = (percentile / 100) * self.DREAD_RISK_CAP

        risk_value = (self.damage + self.affected_users) * (self.reproducibility + self.exploitability + self.discoverability)
        return min(scaled_risk_value, self.DREAD_RISK_CAP)

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
        
        run_random_generator = input("Do you want to run these results against the random generator? (yes/no): ")
        if run_random_generator.lower() == "yes":
                random_result = assessment.run_against_random_generator()
                print("Random Generator Results:")
                table = PrettyTable()
                table.field_names = ["Parameter", "Value"]
                table.add_row(["Random Risk Value", random_result])
                print(table)


    except ValueError:
        print("Invalid input. Please enter numeric values in the specified range.")

if __name__ == "__main__":
    assessments = {}
    main()
