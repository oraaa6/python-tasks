# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
#2 ) Use the datetime library together with the random number to generate a random, unique value.

import random
import datetime


def generate_random_data():
    random_number_below_1 = random.random()
    random_number_above_1 = random.randrange(1, 10)
    print('Random number below 1: {:2f}, Random number above 1: {}'.format(random_number_below_1, random_number_above_1))
    
    random_time_delta = datetime.timedelta(days=random_number_below_1, hours=random_number_above_1, minutes=random_number_above_1)
    print('Random time delta: {}'.format(random_time_delta))
    
    
generate_random_data()
