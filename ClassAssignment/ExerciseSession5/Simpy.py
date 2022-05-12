import simpy
import random
import statistics

print(f'STARTING SIMULATION')
print(f'----------------------------------')

wait_times = []

#containers
    #snaps
snaps_capacity = 150
initial_snaps = 30

#critical levels
    #critical stock should be calculated depending on former data.Here we assume it 100
snaps_critial_stock = 60

class Canteen(object):
    def __init__(self, env, num_foodservers, num_drinkmachines, num_snapssups, num_cashiers):
        self.env = env
        self.foodserver = simpy.Resource(env, num_foodservers)
        self.drinkmachine = simpy.Resource(env, num_drinkmachines)
        self.snapssup = simpy.Resource(env, num_snapssups)
        self.cashier = simpy.Resource(env, num_cashiers)
        self.snap = simpy.Container(env, capacity = snaps_capacity, init = initial_snaps)
        self.snaps_control = env.process(self.snaps_stock_control(env))

    def snaps_stock_control(self, env):
        yield env.timeout(0)
        while True:
            if self.snap.level <= snaps_critial_stock:
                print('snaps stock bellow critical level ({0}) '.format(
                    self.snap.level))
                print('calling snaps supplier')
                print('----------------------------------')
                yield env.timeout(3)
                print('snaps supplier arrives')
                yield self.snap.put(60)
                print('new snaps stock is {0}'.format(
                    self.snap.level))
                print('----------------------------------')
                yield env.timeout(10)
            else:
                yield env.timeout(30)    
        
    def get_food(self, mealgoer):
        yield self.env.timeout(random.randint(1, 2))

    def get_drink(self, mealgoer):
        yield self.env.timeout(random.randint(1, 2))

    def get_snap(self, mealegoer):
        yield self.snap.get(1)
        yield self.env.timeout(30/60)
    #Mealgoer  get a snap

    def get_check(self, mealegoer):
        yield self.env.timeout(20/60)

def go_to_meals(env, mealgoer, canteen):
    # Mealgoer arrives at the canteen
    arrival_time = env.now

    with canteen.foodserver.request() as request:
        yield request
        yield env.process(canteen.get_food(mealgoer))

    if random.choice([True, False]):
        with canteen.drinkmachine.request() as request:
            yield request
            yield env.process(canteen.get_drink(mealgoer))
    
    if random.choice([True, False]):
        with canteen.snapssup.request() as request:
            yield request
            yield env.process(canteen.get_snap(mealgoer))
            
    with canteen.cashier.request() as request:
        yield request
        yield env.process(canteen.get_check(mealgoer))

    # Mealgoer heads into the canteen
    wait_times.append(env.now - arrival_time)


def run_canteen(env, num_foodservers, num_drinkmachines, num_snapssups, num_cashiers):
    canteen = Canteen(env, num_foodservers, num_drinkmachines, num_snapssups, num_cashiers)

    for mealgoer in range(30):
        env.process(go_to_meals(env, mealgoer, canteen))

    while True:
        yield env.timeout(2)  # Wait a bit before generating a new person

        mealgoer += 1
        env.process(go_to_meals(env, mealgoer, canteen))


def get_average_wait_time(wait_times):
    average_wait = statistics.mean(wait_times)
    # Pretty print the results
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)


def get_user_input():
    num_foodservers = input("Input # of foodservers working: ")
    num_drinkmachines = input("Input # of drinkmachiens working: ")
    num_snapssups = input("Input # of snapssuppliers working: ")
    num_cashiers = input("Input # of cashiers working: ")
    params = [num_foodservers, num_drinkmachines, num_snapssups, num_cashiers]
    if all(str(i).isdigit() for i in params):  # Check input is valid
        params = [int(x) for x in params]
    else:
        print(
            "Could not parse input. Simulation will use default values:",
            "\n5 foodservers, 5 drinkmachiens, 5 snapssuppliers, 5 cashiers.",
        )
        params = [5, 5, 5, 5]
    return params


def main():
    # Setup
    random.seed(42)
    num_foodservers, num_drinkmachines, num_snapssups, num_cashiers = get_user_input()

    # Run the simulation
    env = simpy.Environment()
    env.process(run_canteen(env, num_foodservers, num_drinkmachines, num_snapssups, num_cashiers))
    env.run(until=120)

    # View the results
    mins, secs = get_average_wait_time(wait_times)
    print(
        "Running simulation...",
        f"\nThe average wait time is {mins} minutes and {secs} seconds.",
    )


if __name__ == "__main__":
    main()