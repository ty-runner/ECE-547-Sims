import math

def erlang_b(n, A):
    numerator = (A**n) / math.factorial(n)
    denominator = sum((A**k) / math.factorial(k) for k in range(n+1))
    return numerator / denominator

desired_blocking_probability = 0.01
A = 120
n = 0

while True:
    blocking_probability = erlang_b(n, A)
    if blocking_probability < desired_blocking_probability:
        break
    n += 1

print(f"Number of VMs required to achieve a blocking probability < 0.01: {n}")