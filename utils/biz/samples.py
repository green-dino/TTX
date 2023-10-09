import scipy.stats as stats
import math

def calculate_sample_size(margin_of_error, confidence_level, population_size=None):
    # Determine the critical Z-value based on the confidence level
    if confidence_level == 0.95:
        z_critical = 1.96  # Z-value for a 95% confidence level
    elif confidence_level == 0.99:
        z_critical = 2.58  # Z-value for a 99% confidence level
    else:
        print("Unsupported confidence level.")
        return None

    # Calculate the required sample size
    if population_size is not None:
        # Finite population correction
        sample_size = (population_size * z_critical**2) / (
            population_size * z_critical**2 + population_size - 1)
    else:
        # Infinite population (unknown population size)
        sample_size = (z_critical**2) / (margin_of_error**2)

    return math.ceil(sample_size)  # Round up to the nearest whole number

if __name__ == "__main__":
    # Input parameters
    margin_of_error = float(input("Enter the margin of error (as a proportion): "))
    confidence_level = float(input("Enter the confidence level (0.95 for 95%, 0.99 for 99%, etc.): "))
    population_size = float(input("Enter the population size (if known, or enter None for unknown population size): "))

    # Calculate and display the sample size
    sample_size = calculate_sample_size(margin_of_error, confidence_level, population_size)
    if sample_size is not None:
        print(f"Required sample size: {sample_size}")
