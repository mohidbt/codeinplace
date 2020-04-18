from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""

"""
Covers 3 houses with beepers on their outside.
Pre: Karels left-side is blocked by a house wall, facing west
Post:Karel facing west.
"""
def main():
    for i in range(2):
        build_house()
        turn_right()
    build_house()


"""
Puts beepers around 3 borders of a house. 
Pre: Karels left-side blocked by house wall, whilst facing west.
Post:Karels right-side blocked by house wall, whilst facing east.
"""
def build_house():
    for i in range(2):
        build_street()
        turn_left()
        move()
    build_street()


"""
Runs a down a wall while putting beepers.
Pre: Facing east
Post: Facing south
"""
def build_street():
    while left_is_blocked():
        put_beeper()
        move()


"""
Turns Karel to the right.
Pre: Karel facing east.
Post: Karel facing south.
"""
def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
