class BusinessProblem:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.stakeholders = []
        self.root_cause = None
        self.impact = None
        self.solutions = []

    def add_stakeholder(self, stakeholder):
        """Add a stakeholder to the list of stakeholders involved in the problem."""
        self.stakeholders.append(stakeholder)

    def set_root_cause(self, root_cause):
        """Set the root cause of the problem."""
        self.root_cause = root_cause

    def set_impact(self, impact):
        """Set the impact of the problem on the business."""
        self.impact = impact

    def add_solution(self, solution):
        """Add a proposed solution to the problem."""
        self.solutions.append(solution)

    def get_summary(self):
        """Get a summary of the business problem."""
        summary = f"Name: {self.name}\n"
        summary += f"Description: {self.description}\n"
        summary += f"Stakeholders: {', '.join(self.stakeholders)}\n"
        summary += f"Root Cause: {self.root_cause}\n"
        summary += f"Impact: {self.impact}\n"
        summary += f"Solutions: {', '.join(self.solutions)}\n"
        return summary

def create_business_problem():
    name = input("Enter the name of the business problem: ")
    description = input("Enter the description of the business problem: ")

    problem = BusinessProblem(name, description)

    while True:
        print("\nOptions:")
        print("1. Add Stakeholder")
        print("2. Set Root Cause")
        print("3. Set Impact")
        print("4. Add Solution")
        print("5. Finish and Display Summary")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            stakeholder = input("Enter a stakeholder: ")
            problem.add_stakeholder(stakeholder)
        elif choice == "2":
            root_cause = input("Enter the root cause: ")
            problem.set_root_cause(root_cause)
        elif choice == "3":
            impact = input("Enter the impact: ")
            problem.set_impact(impact)
        elif choice == "4":
            solution = input("Enter a solution: ")
            problem.add_solution(solution)
        elif choice == "5":
            print("\nBusiness Problem Summary:")
            print(problem.get_summary())
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    create_business_problem()
