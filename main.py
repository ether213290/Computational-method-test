import numpy as np
# Creator: Jiacheng Li
# Email: lij31@tcd.ie
# Contact me if anything breaks
print("Hello world")

def MSE(a, b):
    for i in range(0, (len(a) - 1)):
        result = np.mean((a[i] - b[i]) ^ 2)
    return result
a = [10, 20, 30, 40, 50]
b = [5, 10, 13, 40, 50]
print(MSE(a, b))