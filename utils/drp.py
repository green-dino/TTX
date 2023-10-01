class DisasterRecoveryPlanGoal:
    def __init__(self, name):
        self.name = name
        self.dependencies = []

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def execute(self):
        print(f"Executing {self.name}")

class DisasterRecoveryProcedure:
    def __init__(self, name):
        self.name = name
        self.dependencies = []

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def execute(self):
        print(f"Executing {self.name}")

class RecoveryPlan:
    def __init__(self, name):
        self.name = name
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def execute(self):
        print(f"Executing {self.name}")
        for step in self.steps:
            step.execute()

# Create instances for each item in the disaster recovery plan
goal_a = DisasterRecoveryPlanGoal("Disaster Recovery Plan Goals")
info_b = DisasterRecoveryPlanGoal("Personnel Information")
profile_c = DisasterRecoveryPlanGoal("Application Profile")
profile_d = DisasterRecoveryPlanGoal("Inventory Profile")
backup_e = DisasterRecoveryPlanGoal("Information Services Backup Procedures")
procedure_f = DisasterRecoveryProcedure("Disaster Recovery Procedures")
plan_g = RecoveryPlan("Recovery Plan for Mobile Site")
plan_h = RecoveryPlan("Recovery Plan for Hot Site")
restore_i = DisasterRecoveryPlanGoal("Restoring the Entire System")
rebuilding_j = DisasterRecoveryPlanGoal("Rebuilding Process")
test_k = DisasterRecoveryPlanGoal("Testing the Disaster Recovery Plan")
rebuilding_l = DisasterRecoveryPlanGoal("Disaster Site Rebuilding")
changes_m = DisasterRecoveryPlanGoal("Record of Plan Changes")

# Define the relationships
goal_a.add_dependency(info_b)
goal_a.add_dependency(profile_c)
goal_a.add_dependency(profile_d)
backup_e.add_dependency(procedure_f)
procedure_f.add_dependency(plan_g)
procedure_f.add_dependency(plan_h)
restore_i.add_dependency(rebuilding_j)

# Define steps for each recovery plan
plan_g.add_step(rebuilding_l)
plan_h.add_step(test_k)
plan_h.add_step(restore_i)
plan_h.add_step(changes_m)

# Execute the disaster recovery plan
goal_a.execute()

