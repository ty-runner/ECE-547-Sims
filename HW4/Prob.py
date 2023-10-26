import simpy
import random
import matplotlib.pyplot as plt

# Parameters
arrival_rate = 5  # Poisson arrival rate
service_rate = 6  # Service rate
simulation_time = 1000  # Total simulation time

# Initialize variables
env = simpy.Environment()
queue = []
n_data = []  # To store n(t) data

def arrival_process(env):
    global queue
    while True:
        interarrival_time = random.expovariate(arrival_rate)
        yield env.timeout(interarrival_time)
        queue.append(env.now)  # Arrival time

def service_process(env):
    global queue
    while True:
        if queue:
            queue.pop(0)  # Remove the first packet (FIFO)
            service_time = random.expovariate(service_rate)
            yield env.timeout(service_time)
        else:
            yield env.timeout(0.01)  # Idle time

def monitor_process(env):
    global n_data
    while True:
        n_data.append(len(queue))
        yield env.timeout(0.1)

# Create and run the simulation
env.process(arrival_process(env))
env.process(service_process(env))
env.process(monitor_process(env))
env.run(until=simulation_time)

# Estimate Pn
total_time = env.now
Pn_estimates = [n_data.count(n) / total_time for n in set(n_data)]

# Estimate E[n]
E_n = sum(n * P for n, P in zip(set(n_data), Pn_estimates))

# Print results
print("Pn estimates:", Pn_estimates)
print("E[n] estimate:", E_n)

# Plot n(t)
plt.plot([i * 0.1 for i in range(len(n_data))], n_data)
plt.xlabel('Time (t)')
plt.ylabel('Number of Packets (n(t))')
plt.title('Queue Length vs. Time')
plt.show()
