import numpy as np


class RandomRisk:
    DREAD_RISK_CAP = 54  # Define your desired risk cap value here

    def __init__(self, damage, reproducibility, exploitability, affected_users, discoverability):
        self.damage = damage
        self.reproducibility = reproducibility
        self.exploitability = exploitability
        self.affected_users = affected_users
        self.discoverability = discoverability

    def calculate_dread_risk(self):
        damage_weight = 0.4
        reproducibility_weight = 0.3
        exploitability_weight = 0.5
        affected_users_weight = 0.01
        discoverability_weight = 0.5

        # Calculate the weighted sum of the parameters
        weighted_sum = (
            self.damage ** damage_weight +
            self.reproducibility ** reproducibility_weight +
            self.exploitability ** exploitability_weight +
            self.affected_users ** affected_users_weight +
            self.discoverability ** discoverability_weight
        )

        # Create a list of all calculated risk values
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

        # Scale the percentile value to fit within your desired range (0 to DREAD_RISK_CAP)
        scaled_risk_value = (percentile / 100) * self.DREAD_RISK_CAP

        risk_value = (self.damage + self.affected_users) * (self.reproducibility + self.exploitability + self.discoverability)
        return min(scaled_risk_value, RandomRisk.DREAD_RISK_CAP)
    
 


