import numpy as np
import matplotlib.pyplot as plt

# Parameters
lambda_ = 5  # Poisson arrival rate
mu_values = [10, 6, 4]  # Service rates: 1/μ (10, 6, 4)
simulation_time = 1000  # Total simulation time

# Initialize simulation variables
time = 0
arrival_times = []
service_times = []
completion_times = []
queue_sizes = []
current_packet = 0  # Represents the current packet in the server

# Simulate the queue for each service rate
for mu in mu_values:
    time = 0  # Reset time for each simulation
    current_packet = 0
    completion_times = []
    queue_sizes = []
    
    while time < simulation_time:
        # Generate next arrival time
        next_arrival_time = time - (1 / lambda_) * np.log(np.random.rand())
        arrival_times.append(next_arrival_time)
        time = next_arrival_time

        # Generate fixed service time
        service_time = 1 / mu
        service_times.append(service_time)

        # Calculate completion time
        if current_packet == 0:
            completion_time = time + service_time
        else:
            completion_time = completion_times[current_packet - 1] + service_time
        completion_times.append(completion_time)

        # Update the current packet and queue size
        current_packet += 1
        queue_sizes.append(current_packet)
    # Plot n(t) for this simulation
    plt.step(completion_times, queue_sizes, where='post', label=f'μ = {1/mu}')
# Plot n(t) for different service rates
plt.xlabel('Time (t)')
plt.ylabel('n(t) (Number of Packets in the Queue)')
plt.title('Queue Simulation with Poisson Arrivals and Different Service Rates')
plt.grid(True)
plt.legend()
plt.show()

# Calculate the average number of packets in the system for each service rate
for mu in mu_values:
    average_packets = np.mean(queue_sizes)
    print(f'Average number of packets in the system (μ = {1/mu}): {average_packets:.2f}')

# Average number of packets in the system (μ = 0.1): 2520.50
# Average number of packets in the system (μ = 0.16666666666666666): 2520.50
# Average number of packets in the system (μ = 0.25): 2520.50