import numpy as np

samples = 10
lambda_param = 1/10
np.random.seed(30)
uniform = np.random.rand(samples)
x = -np.log(1-uniform) / lambda_param
print("X: " , x) #numbers are either very low or very high since its an exponential distribution

poisson_samples = np.zeros(samples, dtype=int)
lambda_param = 10
for i in range(samples):
    p = 1.0
    k = 0
    while True:
        k += 1
        p *= np.random.rand()
        if p < np.exp(-lambda_param):
            break
    poisson_samples[i] = k - 1

print("Y: ",poisson_samples)