import pandas as pd


class ExerciseScenario:
    def __init__(self, name, description, objectives):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.stakeholder_roles = []
        self.discussion_topics = []

    def add_stakeholder_role(self, role_name, role_description):
        role = StakeholderRole(role_name, role_description)
        self.stakeholder_roles.append(role)

    def add_discussion_topic(self, topic, questions):
        discussion_topic = DiscussionTopic(topic, questions)
        self.discussion_topics.append(discussion_topic)

    def introduce_scenario(self):
        introduction = f"Exercise: {self.name}\n"
        introduction += f"Description: {self.description}\n"
        introduction += "Objectives and Goals:\n"
        for i, obj in enumerate(self.objectives, start=1):
            introduction += f"{i}. {obj}\n"
        introduction += "\nStakeholder Roles:\n"
        for role in self.stakeholder_roles:
            introduction += f"- {role}\n"
        introduction += "\nDiscussion Topics:\n"
        for topic in self.discussion_topics:
            introduction += f"{topic}\n"
        return introduction
    
    def add_decision_point(self, point_name, description, options):
        decision_point = DecisionPoint(point_name, description, options)
        self.decision_points.append(decision_point)

class DecisionPoint:
    def __init__(self, point_name, description, options):
        self.point_name = point_name
        self.description = description
        self.options = options
        self.selected_option = None

    def make_decision(self, option_index):
        if 0 <= option_index < len(self.options):
            self.selected_option = self.options[option_index]

    def __str__(self):
        decision_str = f"Decision Point: {self.point_name}\n"
        decision_str += f"Description: {self.description}\n"
        for i, option in enumerate(self.options, start=1):
            decision_str += f"{i}. {option}\n"
        return decision_str

class StakeholderRole:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class DiscussionTopic:
    def __init__(self, topic, questions):
        self.topic = topic
        self.questions = questions

    def __str__(self):
        return f"Topic: {self.topic}\nQuestions: {', '.join(self.questions)}"


# Example usage:

exercise1 = ExerciseScenario(
    name="Cybersecurity Drill",
    description="Simulate a cyberattack on the organization's network.",
    objectives=[
        "Assess the response time to the incident.",
        "Evaluate the effectiveness of the incident response plan.",
        "Identify weaknesses in the network's security measures.",
    ],
)

exercise1.add_stakeholder_role(
    "Incident Commander",
    "Responsible for coordinating the response to the cyberattack."
)

exercise1.add_stakeholder_role(
    "Network Administrator",
    "Responsible for managing and securing the organization's network infrastructure."
)

class AttackTactics:
    def __init__(self):
        self.initial_access = InitialAccess()
        self.execution = Execution()
        self.persistence = Persistence()
        self.privilege_escalation = PrivilegeEscalation()
        self.defense_evasion = DefenseEvasion()
        self.credential_access = CredentialAccess()
        self.discovery = Discovery()
        self.lateral_movement = LateralMovement()
        self.collection = Collection()
        self.exfiltration = Exfiltration()
        self.impact = Impact()

class InitialAccess:
    def __init__(self):
        self.external_remote_services = ExternalRemoteServices()
        self.phishing = Phishing()
        self.hardware_additions = HardwareAdditions()
        self.taint_shared_content = TaintSharedContent()

class Execution:
    def __init__(self):
        self.command_and_script_interpreter = CommandAndScriptInterpreter()
        self.executable_installer = ExecutableInstaller()
        self.rootkit = Rootkit()
        self.taint_shared_content = TaintSharedContent()

class Persistence:
    def __init__(self):
        self.boot_or_logon_autostart_execution = BootOrLogonAutostartExecution()
        self.service_registry_permissions_weakness = ServiceRegistryPermissionsWeakness()
        self.scheduled_task_job = ScheduledTaskJob()
        self.startup_items = StartupItems()
        self.taint_shared_content = TaintSharedContent()

class PrivilegeEscalation:
# continue efforts here later 
