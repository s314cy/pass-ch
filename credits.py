import argparse
from itertools import combinations


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('goal', type=int)
    parser.add_argument('base', type=int, default=0)
    parser.add_argument('-c', '--credits', type=int, nargs='+', required=True)
    args = parser.parse_args()

    assert args.base < args.goal
    assert args.base >= 0 and args.goal > 0

    for r in range(1, len(args.credits) + 1):
        for c in combinations(args.credits, r):
            obtained = args.base + sum(c)
            if obtained >= args.goal:
                print(*c, obtained)
