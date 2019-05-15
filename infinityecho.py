from time import *
from random import *
from string import *

def north(logic):
    print("You head North...")
    sleep(0.5)
    if logic >= 5:
        event = True
    else:
        event = False
    return event

def south(logic):
    print("You head South...")
    sleep(0.5)
    if logic >= 5:
        event = True
    else:
        event = False
    return event


def east(logic):
    print("You head East...")
    sleep(0.5)
    if logic >= 5:
        event = True
    else:
        event = False
    return event


def west(logic):
    print("You head West...")
    sleep(0.5)
    if logic >= 5:
        event = True
    else:
        event = False
    return event


def brain():
    logic = random.randint(1, 10)
    return logic


def encounter(event, mob):
    if event:
        sleep(0.5)
        print("You encounter a " + mob + "!")


def baddie():
    moblow = { "Kobald", "Slime", "Bat", "Wolf", "Jackalope", "Goblin"}
    mob = random.choice(moblow)
    return mob


