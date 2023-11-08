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
import random
import statistics

wait_times = []

class Theater(object):
    def __init__(self, env, num_cashiers, num_servers, num_ushers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.servers = simpy.Resource(env, num_servers)
        self.ushers = simpy.Resource(env, num_ushers)

    def buy_ticket(self, moviegoer):
        yield self.env.timeout(random.randint(1,3))

    def check_ticket(self, moviegoer):
        yield self.env.timeout(3/60)

    def sell_food(self, moviegoer):
        yield self.env.timeout(random.randint(1,5))
        
def moviegoer_behavior(env, moviegoer, theater):
    # moviegoer arrives at the theater
    arrival_time = env.now

    # moviegoer gets in line to buy a ticket
    with theater.cashier.request() as request:
        yield request
        yield env.process(theater.buy_ticket(moviegoer))

    # moviegoer waits in line to have the ticket checked
    with theater.ushers.request() as request:
        yield request
        yield env.process(theater.check_ticket(moviegoer))

    # moviegoer decides to buy concessions
    if random.random() < 0.5:
        # moviegoer gets in line to buy concessions
        with theater.servers.request() as request:
            yield request
            yield env.process(theater.sell_food(moviegoer))

    # moviegoer goes to the theater
    wait_time = env.now - arrival_time
    wait_times.append(wait_time)

# set up the simulation environment
env = simpy.Environment()
theater = Theater(env, num_cashiers=2, num_servers=3, num_ushers=1)

# generate moviegoers and run the simulation
for i in range(50):
    env.process(moviegoer_behavior(env, i, theater))

env.run()

# calculate and print the average wait time
avg_wait_time = statistics.mean(wait_times)
print("Average wait time:", round(avg_wait_time, 2), "minutes")
