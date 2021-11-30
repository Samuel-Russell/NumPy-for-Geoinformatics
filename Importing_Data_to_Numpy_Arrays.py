# Import Packages
import numpy as np

fname = ('average_monthly_temp.txt')

# Import average monthly temperature to numpy array from text file
avg_monthly_temp_nparray = np.loadtxt(fname)

print(avg_monthly_temp_nparray)

# Check type
print(type(avg_monthly_temp_nparray))