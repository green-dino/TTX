class RiskMatrix:
    def __init__(self):
        self.responses = []
        self.questions = [
            "Are unique skills required to complete the attack successfully?",
            "Are significant resources required to complete the attack successfully?",
            "Is it possible that the defense fails to protect against the attack?",
            "Does the defense cover all access points to the asset?",
            "Is the vulnerability always present in the asset?",
            "Are there significant prerequisites to completing the attack successfully?",
            "Is there a significant cost to repair or replace this asset?",
            "Does the asset have significant value to the asset owner?",
            "Will there be consequences to the attack from internal sources?",
            "Will there be consequences to the attack from external sources?"
        ]

    @staticmethod
    def get_yes_or_no_input(question):
        while True:
            user_input = input(f"{question} (yes/no): ").strip().lower()
            if user_input in ["yes", "no"]:
                return user_input
            else:
                print("Please enter 'yes' or 'no'.")

    def collect_responses(self):
        for i, question in enumerate(self.questions):
            response = self.get_yes_or_no_input(f"Question {i}\n{question}")
            self.responses.append(response)

    @staticmethod
    def map_answers_to_matrix(matrix_reference, inputs, matrix_mappings):
        input_str = ''.join(map(str, inputs))
        matrix_name = matrix_mappings.get((matrix_reference, input_str), 'Matrix not found')
        return matrix_name

    def determine_matrices(self):
        matrix_mappings_2x2 = {
            ('A', '00'): 'Threat Scope (L) Large',
            ('B', '23'): 'Protection Capability (B) Incomplete',
            ('D', '45'): 'Occurrence (P) Periodically',
            ('F', '67'): 'Harm (D) Damaging',
            ('G', '89'): 'Valuation (E) Essential',
        }
        matrix_mappings_3x3 = {
            ('C', 'AB'): 'Attack Effectiveness (C) Consistently',
            ('E', 'CD'): 'Threat Likelihood (HL) High Likelihood',
            ('H', 'FE'): 'Impact (Hi) High Impact',
            ('I', 'EH'): 'Risk (H) High',
        }

        matrix_reference_2x2 = 'A'
        matrix_name_2x2 = self.map_answers_to_matrix(matrix_reference_2x2, [self.responses[0], self.responses[1]], matrix_mappings_2x2)

        matrix_reference_3x3 = 'C'
        matrix_name_3x3 = self.map_answers_to_matrix(matrix_reference_3x3, [self.responses[2], self.responses[3]], matrix_mappings_3x3)

        return matrix_name_2x2, matrix_name_3x3


if __name__ == "__main__":
    risk_tool = RiskMatrix()
    
    risk_tool.collect_responses()
    
    matrix_name_2x2, matrix_name_3x3 = risk_tool.determine_matrices()

    print("Collected Responses:")
    for i, response in enumerate(risk_tool.responses):
        print(f"Question {i}: {response}")

    print(f"\nMatrix A Name (2x2): {matrix_name_2x2}")
    print(f"Matrix C Name (3x3): {matrix_name_3x3}")
