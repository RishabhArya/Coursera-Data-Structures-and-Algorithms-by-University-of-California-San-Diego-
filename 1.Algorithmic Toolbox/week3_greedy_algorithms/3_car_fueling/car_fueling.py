# python3
import sys


def compute_min_refills(distance, tank, stops):
    numrefils = 0
    currentposition = 0
    stops.insert(0, 0)
    stops.append(distance)
    stopsnum = len(stops) - 2
    while currentposition <= stopsnum:
        lastposition = currentposition
        while currentposition <= stopsnum and stops[currentposition + 1] - stops[lastposition] <= tank:
            currentposition = currentposition + 1
        if currentposition == lastposition:
            return -1
        if currentposition <= stopsnum:
            numrefils = numrefils + 1
    return numrefils


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
