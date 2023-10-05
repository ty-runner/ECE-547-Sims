# Most programming languages have a function to generate uniform random numbers in the
# interval [0, 1]. For example, in MATLAB, it is the “rand” function. Use this function as a
# basis to generate an exponetially-distributed random variable X and a Poisson-distributed
# random variable Y with E(X) = E(Y ) = 10. Report 10 samples of X. Do you see any
# useful pattern? Do the same for Y . (Please do not directly use more-sophisticated random-
# number generators available in your programming langrage, e.g., those that directly generate
# exponentially-distributed random variables.)

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