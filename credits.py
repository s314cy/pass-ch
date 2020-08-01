import argparse
from itertools import combinations


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('goal', type=int)
    parser.add_argument('base', type=int, default=0)
    parser.add_argument('-c', '--credits', type=int, nargs='+')
    args = parser.parse_args()

    possibilities = []
    for r in range(1, len(args.credits) + 1):
        for c in combinations(args.credits, r):
            possibilities.append(c)
    for p in possibilities:
        if args.base + sum(p) >= args.goal:
            print(*p)
