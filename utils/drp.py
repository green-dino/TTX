import pandas as pd

class Component:
    def __init__(self, name):
        self.name = name
        self.dependencies = []

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def execute(self):
        print(f"Executing {self.name}")

class RecoveryPlan(Component):
    def __init__(self, name):
        super().__init__(name)
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def execute(self):
        super().execute()
        for step in self.steps:
            step.execute()

# Create instances for each item in the disaster recovery plan
goal_a = Component("Disaster Recovery Plan Goals")
info_b = Component("Personnel Information")
profile_c = Component("Application Profile")
profile_d = Component("Inventory Profile")
backup_e = Component("Information Services Backup Procedures")
procedure_f = Component("Disaster Recovery Procedures")
plan_g = RecoveryPlan("Recovery Plan for Mobile Site")
plan_h = RecoveryPlan("Recovery Plan for Hot Site")
restore_i = Component("Restoring the Entire System")
rebuilding_j = Component("Rebuilding Process")
test_k = Component("Testing the Disaster Recovery Plan")
rebuilding_l = Component("Disaster Site Rebuilding")
changes_m = Component("Record of Plan Changes")

# Define the relationships
goal_a.add_dependency(info_b)
goal_a.add_dependency(profile_c)
goal_a.add_dependency(profile_d)
backup_e.add_dependency(procedure_f)
procedure_f.add_dependency(plan_g)
procedure_f.add_dependency(plan_h)
restore_i.add_dependency(rebuilding_j)

# Create a list of dependencies
dependencies = []

def collect_dependencies(item):
    dependencies.append((item.name, [dep.name for dep in item.dependencies]))

collect_dependencies(goal_a)
collect_dependencies(backup_e)
collect_dependencies(restore_i)

# Create a DataFrame from the list of dependencies
drp_df = pd.DataFrame(dependencies, columns=['Item', 'Dependencies'])

# Display the DataFrame
print(drp_df)

# Define steps for each recovery plan
plan_g.add_step(rebuilding_l)
plan_h.add_step(test_k)
plan_h.add_step(restore_i)
plan_h.add_step(changes_m)

# Execute the disaster recovery plan
goal_a.execute()

def execute_disaster_recovery_plan(start_component):
    # Create a stack to keep track of components to execute
    stack = [start_component]

    # Create a set to keep track of executed components to avoid duplicates
    executed_components = set()

    while stack:
        # Pop the next component from the stack
        current_component = stack.pop()

        # Check if the current component has already been executed
        if current_component in executed_components:
            continue

        # Execute the current component
        current_component.execute()

        # Add the dependencies of the current component to the stack
        stack.extend(current_component.dependencies)

        # Mark the current component as executed
        executed_components.add(current_component)

# Call the execute_disaster_recovery_plan function with the starting component
execute_disaster_recovery_plan(goal_a)

