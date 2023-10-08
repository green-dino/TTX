import pandas as pd

# Define the graph structure as a list of tuples
steps = [
    ('A', 'Set the DRP into motion after a disaster has been declared'),
    ('B', 'Determine the magnitude of the disaster'),
    ('C', 'Determine what systems and processes have been affected by the disaster'),
    ('D', 'Communicate the disaster to the other disaster recovery team members'),
    ('E', 'Determine what first steps need to be taken by the disaster recovery teams'),
    ('F', 'Keep the disaster recovery teams on track with pre-determined expectations and goals'),
    ('G', 'Keep a record of money spent during the disaster recovery process'),
    ('H', 'Ensure that all decisions made abide by the DRP and policies set by the company'),
    ('I', 'Ensure that the secondary site is fully functional and secure'),
    ('J', 'Create a detailed report of all the steps undertaken in the disaster recovery process'),
    ('K', 'Notify the relevant parties once the disaster is over and normal business functionality has been restored')
]

# Create a Pandas DataFrame from the graph structure
steps_df = pd.DataFrame(steps, columns=['Task ID', 'Task Description'])

# Define the graph structure as a list of tuples
functions = [
    ('A', 'Disaster identification and declaration', 'B', 'Disaster Recovery Policy DRP activation'),
    ('B', 'Disaster Recovery Policy DRP activation', 'C', 'Assessment of damage'),
    ('C', 'Assessment of damage', 'D', 'Establish IT operations'),
    ('D', 'Establish IT operations', 'E', 'Failover Site activation'),
    ('E', 'Failover Site activation', 'F', 'Communicating the disaster'),
    ('F', 'Communicating the disaster', 'Fa', 'Internal Client Communication'),
    ('F', 'Communicating the disaster', 'Fb', 'Communication with media including social networks')
]

# Create a Pandas DataFrame from the graph structure
functions_df = pd.DataFrame(functions, columns=['From Node', 'From Description', 'To Node', 'To Description'])


import pandas as pd

# Define the graph structure as a list of tuples
roles = [
    ('A', 'Facilitator', 'B', 'Exercise Participants'),
    ('B', 'Exercise Participants', 'C', 'IT Team'),
    ('B', 'Exercise Participants', 'D', 'Management'),
    ('E', 'System Failure', 'F', 'Detection'),
    ('F', 'Detection', 'G', 'Assessment?'),
    ('G', 'Assessment?', 'H', 'Resolution? (Yes)'),
    ('G', 'Assessment?', 'I', 'Communication (No)'),
    ('I', 'Communication (No)', 'F', 'Detection (Loop)'),
    ('H', 'Resolution? (Yes)', 'J', 'Recovery (Yes)'),
    ('H', 'Resolution? (Yes)', 'K', 'Communication (No)'),
    ('K', 'Communication (No)', 'F', 'Detection (Loop)'),
    ('J', 'Recovery (Yes)', 'L', 'After-Action Review'),
    ('M', 'Incident Report', 'N', 'Timeline'),
    ('M', 'Incident Report', 'O', 'Logs'),
    ('O', 'Logs', 'P', 'Anomalies Detected?'),
    ('P', 'Anomalies Detected?', 'Q', 'Root Cause Analysis (Yes)'),
    ('P', 'Anomalies Detected?', 'R', 'Communication (No)'),
    ('S', 'Internal', 'T', 'External'),
    ('T', 'External', 'U', 'Public Disclosure?'),
    ('U', 'Public Disclosure?', 'V', 'PR Response (Yes)'),
    ('U', 'Public Disclosure?', 'W', 'Legal (No)'),
    ('X', 'Evaluation', 'Y', 'Lessons Learned'),
    ('Y', 'Lessons Learned', 'Z', 'Improvements'),
    ('C', 'IT Team', 'E', 'System Failure'),
    ('D', 'Management', 'I', 'Communication'),
    ('I', 'Communication', 'K', 'Communication'),
    ('J', 'Recovery', 'X', 'Evaluation'),
    ('N', 'Timeline', 'R', 'Communication'),
    ('R', 'Communication', 'S', 'Internal'),
    ('Z', 'Improvements', 'C', 'IT Team')
]

# Create a Pandas DataFrame from the graph structure
roles_df = pd.DataFrame(roles, columns=['From Node', 'From Description', 'To Node', 'To Description'])


# Function to filter and display a DataFrame
def filter_and_display(df):
    while True:
        print("\nFilter Options:")
        print("1. Filter by column value")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAvailable columns:")
            for col in df.columns:
                print(col)
            column_name = input("Enter the column name to filter: ")
            filter_value = input("Enter the filter value: ")
            filtered_df = df[df[column_name] == filter_value]
            print("\nFiltered DataFrame:")
            print(filtered_df)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Allow the user to choose which DataFrame to filter
while True:
    print("\nChoose a DataFrame to filter:")
    print("1. Steps")
    print("2. Functions")
    print("3. Roles")
    print("4. Exit")
    data_frame_choice = input("Enter your choice: ")

    if data_frame_choice == '1':
        filter_and_display(steps_df)
    elif data_frame_choice == '2':
        filter_and_display(functions_df)
    elif data_frame_choice == '3':
        filter_and_display(roles_df)
    elif data_frame_choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")






