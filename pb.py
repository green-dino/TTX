from utils.disaster_recovery import steps, roles, functions
import pandas as pd



# Define the graph structure for steps, roles, and functions as you've provided

while True:
    # Prompt the user to select a component type
    print("Select a component type:")
    print("1. Steps")
    print("2. Roles")
    print("3. Functions")
    print("4. Exit")
    component_type = input("Enter the number of the component type you want to view (or 4 to exit): ")

    if component_type == "4":
        print("Exiting the program.")
        break  # Exit the loop if the user chooses to exit

    # Display the selected component based on user input
    if component_type == "1":
        df = pd.DataFrame(steps, columns=['Task ID', 'Task Description'])
    elif component_type == "2":
        df = pd.DataFrame(roles, columns=['From Node', 'From Description', 'To Node', 'To Description'])
    elif component_type == "3":
        df = pd.DataFrame(functions, columns=['From Node', 'From Description', 'To Node', 'To Description'])
    else:
        print("Invalid selection. Please enter a valid option.")
        continue  # Continue to the next iteration of the loop if the input is invalid

    # Print the selected component
    print("Selected Component:")
    print(df)


