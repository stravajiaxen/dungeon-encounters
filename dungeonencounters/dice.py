import random

def roll(a, b=None):
    if b is None:
        return random.randint(1, a)
    else:
        return sum([random.randint(1, b) for _ in range(a)])