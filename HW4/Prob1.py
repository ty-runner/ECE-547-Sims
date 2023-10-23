import random

# Parameters
lambda_val = 5  # Arrival rate
mu_val = 6     # Service rate
simulation_time = 1000  # Total simulation time

# Initialize simulation variables
time = 0
queue_length = 0
event_list = []

# Lists to store Pn and E[n] estimates
max_queue_length = 100  # Set a maximum possible queue length
Pn_estimates = [0] * (10001)
En_estimates = [0] * (simulation_time + 1)
# Main simulation loop
while time < simulation_time:
    # Calculate Pn and En at each time step
    print(time)
    Pn_estimates[queue_length] += 1
    En_estimates[int(time)] = queue_length

    # Generate random exponential inter-arrival and service times
    inter_arrival_time = random.expovariate(lambda_val)
    service_time = random.expovariate(mu_val)

    # Update time
    time += inter_arrival_time

    if time > simulation_time:
        break

    # If an arrival occurs before the simulation time, add it to the queue
    queue_length += 1

    # If service completes before the next arrival, decrement queue
    if service_time < inter_arrival_time:
        queue_length -= 1
    elif queue_length > 0:
        # Otherwise, schedule the next service event
        event_list.append(time + service_time)

# Calculate the final Pn and En estimates
for i in range(len(Pn_estimates)):
    Pn_estimates[i] /= simulation_time

mean_queue_length = sum(En_estimates) / simulation_time

# Compare with M/M/1 queue formulas
rho = lambda_val / mu_val  # Traffic intensity
theoretical_Pn = [(1 - rho) * (rho ** n) for n in range(len(Pn_estimates))]
theoretical_mean_queue_length = rho / (1 - rho)

# Output the results
print("Time\tPn Estimate\tTheoretical Pn")
for t in range(len(Pn_estimates)):
    print(f"{t}\t{Pn_estimates[t]:.4f}\t{theoretical_Pn[t]:.4f}")

print("\nEstimated Mean Queue Length:", mean_queue_length)
print("Theoretical Mean Queue Length:", theoretical_mean_queue_length)