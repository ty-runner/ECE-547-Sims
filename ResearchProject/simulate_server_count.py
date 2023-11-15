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

# Function to run the simulation with varying numbers of servers
def run_simulation(num_servers):
    env = simpy.Environment()
    theater = Theater(env, NUM_CASHIERS, num_servers, NUM_USHERS)
    wait_times = []

    for i in range(50):
        env.process(moviegoer_behavior(env, i, theater, wait_times))
    
    env.run()
    avg_wait_time = statistics.mean(wait_times)
    return avg_wait_time

# Run simulations with different numbers of servers
avg_wait_time = run_simulation(NUM_SERVERS)
while avg_wait_time > 10 and NUM_SERVERS < 20:
    avg_wait_time = run_simulation(NUM_SERVERS)
    wait_times_list.append(round(avg_wait_time, 2))
    print("Average wait time with", NUM_SERVERS, "servers:", round(avg_wait_time, 2), "minutes")
    NUM_SERVERS += 1

plt.plot(range(2, NUM_SERVERS-1), wait_times_list, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Servers')
plt.ylabel('Average Wait Time (minutes)')
plt.title('Impact of Number of Servers on Average Wait Time')
plt.show()

#ALMOST NO CORRELATION BETWEEN NUMBER OF SERVERS AND AVERAGE WAIT TIME BECAUSE THE RANDINT IS RANGED FROM 1-5