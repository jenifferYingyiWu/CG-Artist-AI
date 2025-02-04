import numpy as np
import pandas as pd
from pysfa import SFA
from pysfa.dataset import load_Tim_Coelli_frontier
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Step 1: Load the dataset (Tim Coelli frontier 4.1 dataset)
df = load_Tim_Coelli_frontier(x_select=['labour', 'capital'], y_select=['output'])

# Step 2: Apply logarithmic transformation on data
y = np.log(df.y)  # Output
x = np.log(df.x)  # Inputs (labour, capital)

# Step 3: Initialize and configure the SFA model
sfa = SFA.SFA(y, x, fun=SFA.FUN_PROD, method=SFA.TE_teJ)

# Step 4: Optimize the SFA model to find slow features
sfa.optimize()
print(dir(sfa))

# Step 5: Access the coefficients (beta) and lambda values
beta = sfa.get_beta()  # Coefficients, might be related to slow features
lambda_ = sfa.get_lambda()  # Lambda values, might indicate feature transformation properties

# Step 6: Visualize the slow features using beta (coefficients) as a proxy
plt.plot(beta)  # Plot the beta values
plt.title("Slow Feature Analysis (SFA) - Beta Coefficients")
plt.xlabel("Time / Data Points")
plt.ylabel("Beta Coefficients (Proxy for Slow Features)")
plt.show()

# Optionally, you can also check the lambda values
plt.plot(lambda_)
plt.title("Slow Feature Analysis (SFA) - Lambda Values")
plt.xlabel("Time / Data Points")
plt.ylabel("Lambda Values")
plt.show()
