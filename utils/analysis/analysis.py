# Normal Distribution

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

sns.set_style("whitegrid")


# Generate Gaussian distributed data
np.random.seed(0)
data = np.random.normal(loc=0, scale=1, size=1000)  # mean=0, std=1

# Fit Gaussian distribution using statsmodels
kde = sm.nonparametric.KDEUnivariate(data)
kde.fit()

# Plotting
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.5, label='Data')
plt.plot(kde.support, kde.density, lw=2, label='PDF')
plt.title('Gaussian Distribution')
plt.xlabel('X')
plt.ylabel('Density')
plt.legend()
plt.show()