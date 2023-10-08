import statistics
from collections import Counter

def calculate_mean(numbers):
    if len(numbers) == 0:
        return None
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

def calculate_median(numbers):
    return statistics.median(numbers)

def calculate_quartiles(numbers):
    return statistics.median(numbers[:len(numbers)//2]), statistics.median(numbers), statistics.median(numbers[(len(numbers)+1)//2:])

def calculate_mode(numbers):
    counts = Counter(numbers)
    max_count = max(counts.values())
    mode = [num for num, count in counts.items() if count == max_count]
    return mode

def run_risk_calculator():
    results = {}

    while True:
        print("Select an option:")
        print("1. Calculate Mean")
        print("2. Calculate Median")
        print("3. Calculate Quartiles")
        print("4. Calculate Mode")
        print("5. View Saved Results")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice in {'1', '2', '3', '4'}:
            input_str = input("Enter a series of numbers separated by spaces: ")
            numbers = [float(x) for x in input_str.split()]

            if choice == '1':
                result = calculate_mean(numbers)
                result_name = "Mean"
            elif choice == '2':
                result = calculate_median(numbers)
                result_name = "Median"
            elif choice == '3':
                q1, q2, q3 = calculate_quartiles(numbers)
                result = {'Q1': q1, 'Q2': q2, 'Q3': q3}
                result_name = "Quartiles"
            elif choice == '4':
                modes = calculate_mode(numbers)
                if len(modes) == 1:
                    result = modes[0]
                else:
                    result = modes
                result_name = "Mode(s)"

            name = input("Enter a name for this result: ")
            results[name] = {result_name: result}
            print(f"The {result_name} of the numbers is: {result} (saved as '{name}')")

        elif choice == '5':
            print("Saved Results:")
            for name, result in results.items():
                print(f"{name}: {result}")

        elif choice == '6':
            break  # Quit the program

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    run_risk_calculator()
