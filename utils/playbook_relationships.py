import pandas as pd

# Create a list of relationships
relationships = [
    ('A', 'Change Control Record', 'has', 'B', 'Change request number'),
    ('A', 'Change Control Record', 'has', 'C', 'Change request date'),
    ('A', 'Change Control Record', 'has', 'D', 'Requested by - name and position'),
    ('A', 'Change Control Record', 'has', 'E', 'Description of the change'),
    ('A', 'Change Control Record', 'has', 'F', 'Justification for the change'),
    ('A', 'Change Control Record', 'has', 'G', 'Impact assessment - including potential risks and mitigation measures'),
    ('A', 'Change Control Record', 'has', 'H', 'Change priority - e.g., low, medium, high'),
    ('A', 'Change Control Record', 'has', 'I', 'Change category - e.g., hardware, software, procedural'),
    ('A', 'Change Control Record', 'has', 'J', 'Change implementation date/time'),
    ('A', 'Change Control Record', 'has', 'K', 'Change approver and approval date'),
    ('L', 'Document Control Information', 'has', 'M', 'Document title'),
    ('L', 'Document Control Information', 'has', 'N', 'Document number'),
    ('L', 'Document Control Information', 'has', 'O', 'Revision history'),
    ('L', 'Document Control Information', 'has', 'P', 'Date of last revision'),
    ('L', 'Document Control Information', 'has', 'Q', 'Document owner'),
    ('L', 'Document Control Information', 'has', 'R', 'Distribution list'),
    ('A', 'Change Control Record', 'has', 'L', 'Document Control Information'),
    ('X', 'Change Implementation Plan', 'has', 'Y', 'Scope of the change'),
    ('X', 'Change Implementation Plan', 'has', 'Z', 'Steps involved in implementing the change'),
    ('X', 'Change Implementation Plan', 'has', 'A1', 'Resources required for the change'),
    ('X', 'Change Implementation Plan', 'has', 'B1', 'Timeline for each step'),
    ('X', 'Change Implementation Plan', 'has', 'C1', 'Testing and validation procedures'),
    ('X', 'Change Implementation Plan', 'has', 'D1', 'Rollback plan'),
    ('A', 'Change Control Record', 'has', 'X', 'Change Implementation Plan'),
    ('E1', 'Communication and Notification', 'has', 'F1', 'Stakeholders affected by the change'),
    ('E1', 'Communication and Notification', 'has', 'G1', 'Communication plan'),
    ('E1', 'Communication and Notification', 'has', 'H1', 'Notification process for impacted parties'),
    ('E1', 'Communication and Notification', 'has', 'I1', 'Training requirements for personnel involved in the change'),
    ('A', 'Change Control Record', 'has', 'E1', 'Communication and Notification'),
    ('A2', 'Risk Assessment and Control', 'has', 'B2', 'Risk assessment of the change'),
    ('A2', 'Risk Assessment and Control', 'has', 'C2', 'Identification of potential risks and vulnerabilities'),
    ('A2', 'Risk Assessment and Control', 'has', 'D2', 'Risk mitigation measures'),
    ('A2', 'Risk Assessment and Control', 'has', 'E2', 'Contingency plans for unforeseen issues or failures'),
    ('A2', 'Risk Assessment and Control', 'has', 'F2', 'Monitoring and reporting mechanisms during the change implementation'),
    ('A', 'Change Control Record', 'has', 'A2', 'Risk Assessment and Control'),
    ('A3', 'Document references', 'has', 'B3', 'Documented evidence and artifacts'),
    ('A3', 'Document references', 'has', 'C3', 'Record keeping requirements'),
    ('A3', 'Document references', 'has', 'D3', 'Retention period'),
    ('A', 'Change Control Record', 'has', 'A3', 'Document references'),
    ('A', 'Change Control Record', 'has', 'B', 'Change request number'),
    ('A', 'Change Control Record', 'has', 'C', 'Change request date'),
    ('A', 'Change Control Record', 'has', 'D', 'Requested by - name and position')
]

# Create a pandas DataFrame
pb_relations_df = pd.DataFrame(relationships, columns=['From Node', 'From Entity', 'Relationship', 'To Node', 'To Entity'])

# Display the DataFrame
print(pb_relations_df)
