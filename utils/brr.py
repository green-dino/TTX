# Uses
# Binary Risk Analysis is good for:
# Quick risk conversations - be able to discuss a specific risk in just a few minutes
# Highlighting subjectivity - helping identify where perceptions about risk elements differ
class RiskMatrix:
    def __init__(self):
        self.responses = []
        self.questions = {
            0: "Are unique skills required to complete the attack successfully?",
            1: "Are significant resources required to complete the attack successfully?",
            2: "Is it possible that the defense fails to protect against the attack?",
            3: "Does the defense cover all access points to the asset?",
            4: "Is the vulnerability always present in the asset?",
            5: "Are there significant prerequisites to completing the attack successfully?",
            6: "Is there a significant cost to repair or replace this asset?",
            7: "Does the asset have significant value to the asset owner?",
            8: "Will there be consequences to the attack from internal sources?",
            9: "Will there be consequences to the attack from external sources?"
        }

        self.matrix_mappings = {
    'A': {'00': 'Threat Scope (S) Small', '01': 'Threat Scope (M) Medium', '10': 'Threat Scope (M) Medium', '11': 'Threat Scope (L) Large'},
    'B': {'00': 'Protection Capability (C) Complete', '01': 'Protection Capability (P) Partial', '10': 'Protection Capability (P) Partial', '11': 'Protection Capability (I) Incomplete'},
    'C': {'A0B0': 'Attack Effectiveness (L) Limited Basis', 'A0B1': 'Attack Effectiveness (O) Occasionally', 'A1B0': 'Attack Effectiveness (O) Occasionally', 'A1B1': 'Attack Effectiveness (C) Consistently'},
    'D': {'00': 'Occurrence (R) Rarely', '01': 'Occurrence (P) Periodically', '10': 'Occurrence (P) Periodically', '11': 'Occurrence (A) Always'},
    'E': {'CD': 'Threat Likelihood (LL) Low', 'CP': 'Threat Likelihood (ML) Moderate', 'CO': 'Threat Likelihood (ML) Moderate', 'PD': 'Threat Likelihood (HL) High', 'PP': 'Threat Likelihood (HL) High', 'PO': 'Threat Likelihood (HL) High', 'OD': 'Threat Likelihood (HL) High', 'OP': 'Threat Likelihood (HL) High', 'OO': 'Threat Likelihood (HL) High'},
    'F': {'00': 'Harm (L) Limited', '01': 'Harm (M) Material', '10': 'Harm (M) Material', '11': 'Harm (D) Damaging'},
    'G': {'00': 'Valuation (P) Peripheral', '01': 'Valuation (S) Supporting', '10': 'Valuation (S) Supporting', '11': 'Valuation (E) Essential'},
    'H': {'FG': 'Impact (Li) Low', 'FM': 'Impact (Mi) Moderate', 'FH': 'Impact (Hi) High', 'SG': 'Impact (Mi) Moderate', 'SM': 'Impact (Hi) High', 'SH': 'Impact (Hi) High', 'EG': 'Impact (Hi) High', 'EM': 'Impact (Hi) High', 'EH': 'Impact (Hi) High'},
    'I': {'EH': 'Risk (L) Low', 'EM': 'Risk (M) Moderate', 'EG': 'Risk (M) Moderate', 'SH': 'Risk (M) Moderate', 'SM': 'Risk (H) High', 'SG': 'Risk (H) High', 'FH': 'Risk (H) High', 'FM': 'Risk (H) High', 'FG': 'Risk (H) High'},
}

        self.matrix_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', ]

    def map_answers_to_matrix(self, matrix_reference, inputs):
        input_str = ''.join(map(str, inputs))
        matrix_name = self.matrix_mappings.get(matrix_reference, {}).get(input_str, 'Matrix not found')
        return matrix_name

    @staticmethod
    def get_yes_or_no_input(question):
        while True:
            user_input = input(f"{question} (yes/no): ").strip().lower()
            if user_input in ["yes", "no"]:
                return user_input
            else:
                print("Please enter 'yes' or 'no'.")

    def collect_responses(self):
        for question_number in range(10):
            response = self.get_yes_or_no_input(f"Question {question_number}\n{self.questions[question_number]}")
            self.responses.append(response)

    def map_answers_to_matrix(self, matrix_reference, inputs):
        input_str = ''.join(map(str, inputs))
        matrix_name = self.matrix_mappings.get(matrix_reference, {}).get(input_str, 'Matrix not found')
        return matrix_name

    def determine_matrices(self):
        matrix_names = {}
        for matrix_reference in self.matrix_order:
            responses = [self.responses[i] for i in range(10) if i % 2 == 0]  # Get every other response
            matrix_name = self.map_answers_to_matrix(matrix_reference, responses)
            matrix_names[matrix_reference] = matrix_name

        return matrix_names

if __name__ == "__main__":
    risk_tool = RiskMatrix()

    risk_tool.collect_responses()

    matrix_names = risk_tool.determine_matrices()

    print("Collected Responses:")
    for i, response in enumerate(risk_tool.responses):
        print(f"Question {i}: {response}")

    # Map answers to the 2x2 matrices
    matrix_reference_2x2 = ['A', 'B', 'D', 'F', 'G']
    inputs_2x2 = [
        [risk_tool.responses[0], risk_tool.responses[1]],
        [risk_tool.responses[2], risk_tool.responses[3]],
        [risk_tool.responses[4], risk_tool.responses[5]],
        [risk_tool.responses[6], risk_tool.responses[7]],
        [risk_tool.responses[8], risk_tool.responses[9]]
    ]

    print("\nMapping Answers to 2x2 Matrices:")
    for i, matrix_ref in enumerate(matrix_reference_2x2):
        matrix_name_2x2 = risk_tool.map_answers_to_matrix(matrix_ref, inputs_2x2[i])
        print(f"Matrix {matrix_ref} Name (2x2): {matrix_name_2x2}")

    # Print matrix names from the determine_matrices method
    for matrix_reference, matrix_name in matrix_names.items():
        print(f"\nMatrix {matrix_reference} Name (3x3): {matrix_name}")

    # Map answers to the 3x3 matrices
    matrix_reference_3x3 = ['C', 'E', 'H', 'I']
    inputs_3x3 = [
        ['A', 'B'],
        ['C', 'D'],
        ['F', 'G'],
        ['E', 'H']
    ]

    print("\nMapping Answers to 3x3 Matrices:")
    for i, matrix_ref in enumerate(matrix_reference_3x3):
        matrix_name_3x3 = risk_tool.map_answers_to_matrix(matrix_ref, inputs_3x3[i])
        print(f"Matrix {matrix_ref} Name (3x3): {matrix_name_3x3}")