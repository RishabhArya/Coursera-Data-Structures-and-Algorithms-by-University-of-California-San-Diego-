# python3
import sys


def compute_min_refills(distance, tank, stops):
    totalstopstaken = 0
    stops.append(distance)
    length = len(stops)

    return totalstopstaken


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
