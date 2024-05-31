import random

def roll_die(sides: int) -> int:
    return random.randint(1, sides)

def roll_6die() -> int:
    return roll_die(6)