#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    a=True
    for i in range(12):
        fill_cell()
        for i in range(26):
            if a:
                move_right()
            else:
                move_left()
            fill_cell()
        move_down()

        a = not a

    pass


if __name__ == '__main__':
    run_tasks()
