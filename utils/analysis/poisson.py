import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Generate Poisson distributed data
lambda_param = 5
data = np.random.poisson(lambda_param, 1000)

# Calculate PMF using statsmodels
unique, counts = np.unique(data, return_counts=True)
pmf = counts / len(data)

# Plotting
plt.bar(unique, pmf)
plt.title('Poisson Distribution PMF')
plt.xlabel('X')
plt.ylabel('Probability')
plt.show()