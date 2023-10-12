import pandas as pd
import matplotlib.pyplot as plt


# Sample data for demonstration
data = {
    "Operational database": ["Transaction 1", "Transaction 2", "Transaction 3", None],
    "Manufacturing and production database": ["Production 1", "Production 2", None, "Production 4"],
    "HR and finance database": ["HR Data 1", None, "HR Data 3", "HR Data 4"],
    "IT database": [None, "IT Data 2", "IT Data 3", "IT Data 4"],
    "Data warehouse": ["Data 1", "Data 2", "Data 3", "Data 4"],
    "NoSQL database": ["NoSQL Data 1", "NoSQL Data 2", "NoSQL Data 3", "NoSQL Data 4"]
}

# Function to preprocess and clean data for a specific data type
def preprocess_data(data_type, data):
    # Create a DataFrame from the input data
    df = pd.DataFrame({data_type: data})

    # Handling missing values
    df[data_type].fillna("N/A", inplace=True)

    # Other data preprocessing tasks can be added here

    # Display cleaned data
    print(f"Cleaned {data_type} Data:")
    print(df)
    print("\n")

if __name__ == "__main__":
    # Loop through different data types and preprocess data
    data_types = [
        "Operational database",
        "Manufacturing and production database",
        "HR and finance database",
        "IT database",
        "Data warehouse",
        "NoSQL database"
    ]

    for data_type in data_types:
        preprocess_data(data_type, data[data_type])

