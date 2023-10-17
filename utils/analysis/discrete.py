import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Generate uniform discrete distributed data
np.random.seed(0)
data = np.random.randint(1, 7, size=1000)  # Simulating a fair 6-sided die

# Fit uniform discrete distribution using statsmodels
ecdf = sm.distributions.ECDF(data)

# Plotting
plt.figure(figsize=(10, 6))
plt.step(ecdf.x, ecdf.y, where='post', label='ECDF')
plt.title('Uniform Discrete Distribution')
plt.xlabel('X')
plt.ylabel('Probability')
plt.legend()
plt.show()