"""
File: PotholeFilling.py
Name: Mark:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Mark:
    """
    pass
    move()
    for i in range(3):
        turn_left()
    move()
    for i in range(99):
        put_beeper()
    for i in range(2):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    move()
    for i in range(3):
        turn_left()
    move()
    for i in range(99):
        put_beeper()
    for i in range(2):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    move()
    for i in range(3):
        turn_left()
    move()
    for i in range(99):
        put_beeper()
    for i in range(2):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
