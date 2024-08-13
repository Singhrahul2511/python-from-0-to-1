import random 
import time
random.seed(6)
fix_seed = 6
rand_num_fix_seed = [random.randint(10,50) for i in range(5)]
print(f"ran value {rand_num_fix_seed}: ")

seed_time = int(time.time())
random.seed(seed_time)
ran_num_time_seed = [random.randint(10,50) for i in range(5)]
print(f"random value with time_based seed {ran_num_time_seed}")
print(f"seed value associated with time {seed_time}")