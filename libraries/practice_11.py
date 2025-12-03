## Python Libraries

import math

def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# math.factorial(n) does the same job as the custom factorial function,
# but much faster and optimized.
print(math.factorial(5))   # Example usage


import pandas as pd
import numpy as np

# Example of loading a CSV file with pandas into a DataFrame
# df = pd.read_csv("file.csv")

# Generate 3 random numbers between 0 and 1 using NumPy
np.random.rand(3)

