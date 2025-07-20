import random

def roll_dice(sides=20):
    return random.randint(1, sides)

def generate_event():
    events = [
        "You enter a dark forest 🌲",
        "A mysterious figure approaches 🧙‍♂️",
        "You find a glowing chest ✨",
        "A dragon roars nearby 🐉",
        "You step into ancient ruins 🏛️"
    ]
    return random.choice(events)
