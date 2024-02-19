import time
import random

def simulate_external_request():
    time.sleep(random.randint(1, 60))
    return random.choice([True, False])
