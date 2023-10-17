import argparse

class ProcessFlow:
    def __init__(self):
        self.current_step = None

    def start(self):
        self.current_step = "Start"
        print(self.current_step)
        self.user_choice()

    def user_choice(self):
        user_input = input("Enter 'C' for WorkRole, 'E' for Change, or 'F' for Request: ")
        if user_input == 'C':
            self.work_role()
        elif user_input == 'E':
            self.change()
        elif user_input == 'F':
            self.request()
        else:
            print("Invalid input. Please enter 'C', 'E', or 'F'.")
            self.user_choice()

    def work_role(self):
        self.current_step = "WorkRole"
        print(self.current_step)
        user_input = input("Enter 'D' for Problem, 'E' for Change, or 'F' for Request: ")
        if user_input == 'D':
            self.problem()
        elif user_input == 'E':
            self.change()
        elif user_input == 'F':
            self.request()
        else:
            print("Invalid input. Please enter 'D', 'E', or 'F'.")
            self.work_role()

    def request(self):
        self.current_step = "Request"
        print(self.current_step)
        self.control_record()

    def problem(self):
        self.current_step = "Problem"
        print(self.current_step)
        # Implement the logic for handling a problem here, if needed.
        self.end_process()

    def change(self):
        self.current_step = "Change"
        print(self.current_step)
        user_input = input("Enter 'M' for Fulfillment or 'N' for ProblemResolution: ")
        if user_input == 'M':
            self.fulfillment()
        elif user_input == 'N':
            self.problem_resolution()
        else:
            print("Invalid input. Please enter 'M' or 'N'.")
            self.change()

    def fulfillment(self):
        self.current_step = "Fulfillment"
        print(self.current_step)
        # Implement the logic for change fulfillment here, if needed.
        self.end_process()

    def problem_resolution(self):
        self.current_step = "ProblemResolution"
        print(self.current_step)
        # Implement the logic for problem resolution here, if needed.
        self.end_process()

    def control_record(self):
        self.current_step = "ControlRecord"
        print(self.current_step)
        # Implement the logic for managing a control record here, if needed.
        self.end_process()

    def end_process(self):
        self.current_step = "End"
        print(self.current_step)

def main():
    parser = argparse.ArgumentParser(description="Process Flow Application")
    parser.add_argument("--start", action="store_true", help="Start the process flow")

    args = parser.parse_args()

    if args.start:
        flow = ProcessFlow()
        flow.start()

if __name__ == "__main__":
    main()
