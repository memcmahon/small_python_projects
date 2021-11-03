"""Bouncing Logo"""

import sys, random, time, bext

WIDTH, HEIGHT   = bext.size()
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT    = 0.2
COLORS          = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT   = 'ur'
UP_LEFT    = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT  = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

COLOR = 'color'
X     = 'x'
Y     = 'y'
DIR   = 'direction'


def main():
    bext.clear()

    logos = []
    for i in rance(NUMBER_OF_LOGOS):
        logos.append(
            {COLOR: random.choice(COLORS),
             X: random.randint(1, WIDTH - 4),
             Y: random.rand_int(1, HEIGHT - 4),
             DIR: random.choice(DIRECTIONS)
            }
        )
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1

    cornerBounces = 0
    # while TRUE:


if __name__ == '__main__':
    main()
