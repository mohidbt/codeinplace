from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

"""
Pre: Karel is at bottom on column, facing east.
Post: Karel is at bottom on column, facing east.
"""
def main():
    for i in range(3):
        run_one_further()


"""
Lets Karel run up / build current and next column of arch.
Pre: Karel faces east, is at bottom of column.
Post: Karel faces east, is at bottom of column.
"""
def run_one_further():
    turn_left()
    run_up()
    turn_right()
    four_step()
    turn_right()
    run_up()
    turn_left()


"""
Karel rebuilds a column.
Pre: Karel faces east, is at bottom of column.
Post: Karel faces north, is at top of column.
"""
def run_up():
    for i in range(4):
        if beepers_present():
            move()
        else:
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


"""
Karel moves four times.
Pre: /
Post: /
"""
def four_step():
    for i in range(4):
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
