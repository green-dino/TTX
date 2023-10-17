import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import expon

# Generate exponentially distributed data
np.random.seed(0)
data = np.random.exponential(scale=1.0, size=1000)

# Plot histogram of the data
plt.hist(data, bins=30, density=True, alpha=0.5, label='Data')

# Fit exponential distribution using statsmodels
ecdf = sm.distributions.ECDF(data)
x = np.linspace(min(data), max(data), 1000)
y = ecdf(x)

# Plot the fitted exponential distribution
plt.plot(x, y, label='Fitted Exponential Cummulative Distribution Function')

# Plot the PDF of the exponential distribution for comparison
pdf_x = np.linspace(min(data), max(data), 1000)
pdf_y = expon.pdf(pdf_x)
plt.plot(pdf_x, pdf_y, label='Exponential PDF')

plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.title('Exponential Distribution Example with PDF')
plt.show()
