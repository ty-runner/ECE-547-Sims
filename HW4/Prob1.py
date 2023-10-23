import math

blocking_probability = 0.01
arrival_rate = 40
mean_service_time = 3
A = arrival_rate * (1 / mean_service_time)
N = 1

while True:
    B = (A ** N) / math.factorial(N)
    if B < blocking_probability:
        break
    N += 1

print("Number of VMs required to meet blocking probability < 0.01:", N)