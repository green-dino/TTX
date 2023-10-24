
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Generate log-normally distributed data
np.random.seed(0)
data = np.random.lognormal(mean=0, sigma=1, size=1000)  # mean=0, std=1

# Fit log-normal distribution using statsmodels
kde = sm.nonparametric.KDEUnivariate(np.log(data))
kde.fit()

# Plotting
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.5, label='Data')
plt.plot(np.exp(kde.support), kde.density / np.exp(kde.support), lw=2, label='PDF')
plt.title('Log-Normal Distribution')
plt.xlabel('X')
plt.ylabel('Density')
plt.legend()
plt.show()