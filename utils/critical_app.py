import csv
import os


class CriticalApplication:
    def __init__(self, name, description, owner, status):
        self.Name = name  # Uppercase with bumpy caps
        self.Description = description
        self.Owner = owner
        self.Status = status  # Active voice

    def __str__(self):
        return f"Name: {self.Name}\nDescription: {self.Description}\nOwner: {self.Owner}\nStatus: {self.Status}"

# Create an empty list to store the critical applications
critical_apps = []

# Prompt the user to input details for a critical application
while True:
    name = input("Enter the name of the critical application: ")
    description = input("Enter the description of the application: ")
    owner = input("Enter the owner of the application: ")
    status = input("Enter the status of the application (Active/Inactive): ")

    # Create an instance of CriticalApplication with the user's input
    app = CriticalApplication(name, description, owner, status)

    # Add the application to the list
    critical_apps.append(app)

    # Ask the user if they want to add another application
    another_app = input("Do you want to add another critical application? (yes/no): ").lower()
    if another_app != "yes":
        break

# Define the path to the CSV file directly under the "docs" directory
csv_file_path = os.path.join("docs", "critical_app.csv")

# Write the critical application data to a CSV file in the "docs" directory
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["Name", "Description", "Owner", "Status"])
    # Write the data for each application
    for app in critical_apps:
        writer.writerow([app.Name, app.Description, app.Owner, app.Status])

print(f"The data has been saved to '{csv_file_path}'.")
