# Movie Theater Sim

# Goal - Average Wait - 10 mins or less

#arrive at theater
#git in line to buy ticket
#buy ticket
#wait in line to have ticket checked
#have ticket checked
#decide to buy concessions
#wait in line to buy concessions or go directly to seats

import simpy
import statistics
from theater import Theater
from moviegoer import moviegoer_behavior
import matplotlib.pyplot as plt

wait_times_list = []
NUM_CASHIERS = 2
NUM_SERVERS = 3
NUM_USHERS = 1

# Function to run the simulation with varying numbers of cashiers
def run_simulation(num_cashiers):
    env = simpy.Environment()
    theater = Theater(env, num_cashiers, NUM_SERVERS, NUM_USHERS)
    wait_times = []

    for i in range(50):
        env.process(moviegoer_behavior(env, i, theater, wait_times))
    
    env.run()
    avg_wait_time = statistics.mean(wait_times)
    return avg_wait_time

# Run simulations with different numbers of cashiers
avg_wait_time = run_simulation(NUM_CASHIERS)
while avg_wait_time > 10:
    avg_wait_time = run_simulation(NUM_CASHIERS)
    wait_times_list.append(round(avg_wait_time, 2))
    print("Average wait time with", NUM_CASHIERS, "cashiers:", round(avg_wait_time, 2), "minutes")
    NUM_CASHIERS += 1
plt.plot(range(2, NUM_CASHIERS), wait_times_list, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Cashiers')
plt.ylabel('Average Wait Time (minutes)')
plt.title('Impact of Number of Cashiers on Average Wait Time')
plt.show()
