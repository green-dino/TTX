from utils.biz import scope

def create_business_problem():
    name = input("enter the name of the business problem")
    description =input("describe the problem")

    problem = scope.BusinessProblem(name,description)

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
