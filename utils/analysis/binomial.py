import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Generate Binomial distributed data
n_trials = 10
p_success = 0.5
data = np.random.binomial(n_trials, p_success, 1000)

# Calculate PMF using statsmodels
unique, counts = np.unique(data, return_counts=True)
pmf = counts / len(data)

# Plotting
plt.bar(unique, pmf)
plt.title('Binomial Distribution PMF')
plt.xlabel('X')
plt.ylabel('Probability')
plt.show()