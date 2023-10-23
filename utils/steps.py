class PDQFramework:
    def __init__(self):
        self.steps = {}

    def add_step(self, step_number, chapter_title, description):
        self.steps[step_number] = {
            'chapter_title': chapter_title,
            'description': description
        }

    def planning_steps(self):
        planning_steps = [self.steps[i] for i in range(1, 7)]
        return planning_steps

    def evaluation_and_improvement_steps(self):
        evaluation_steps = [self.steps[i] for i in range(7, 11)]
        return evaluation_steps

# Create an instance of the PDQFramework
pdq = PDQFramework()

# Add steps to the PDQ framework
pdq.add_step(1, "Chapter One: Step 1 - Assessing Problems and Resources", "Description of Step 1")
pdq.add_step(2, "Chapter Two: Step 2 - Setting Goals and Desired Outcomes for a Prevention Activity", "Description of Step 2")
pdq.add_step(3, "Chapter Three: Step 3 - Evidence-Based and Promising Practices in Prevention", "Description of Step 3")
pdq.add_step(4, "Chapter Four: Step 4 - Assessing Fit for a Prevention Activity", "Description of Step 4")
pdq.add_step(5, "Chapter Five: Step 5 - Determining Capacity to Implement a Prevention Activity", "Description of Step 5")
pdq.add_step(6, "Chapter Six: Step 6 - Planning to Implement and Evaluate a Prevention", "Description of Step 6")
pdq.add_step(7, "Chapter Seven: Step 7 - Process Evaluation for a Prevention", "Description of Step 7")
pdq.add_step(8, "Chapter Eight: Step 8 - Outcome Evaluation for Prevention", "Description of Step 8")
pdq.add_step(9, "Chapter Nine: Step 9 - Continuous Quality Improvement CQI", "Description of Step 9")
pdq.add_step(10, "Chapter Ten: Step 10 - Sustainability for a Prevention Activity", "Description of Step 10")

# Define the planning and evaluation/improvement functions
def planning():
    planning_steps = pdq.planning_steps()
    for step in planning_steps:
        print(f"Planning Step {list(pdq.steps.keys())[list(pdq.steps.values()).index(step)]}: {step['chapter_title']}")
        print(step['description'])
        print()

def evaluation_and_improvement():
    evaluation_steps = pdq.evaluation_and_improvement_steps()
    for step in evaluation_steps:
        print(f"Evaluation/Improvement Step {list(pdq.steps.keys())[list(pdq.steps.values()).index(step)]}: {step['chapter_title']}")
        print(step['description'])
        print()

# Call the functions
print("Planning Steps:")
planning()

print("Evaluation and Improvement Steps:")
evaluation_and_improvement()
