# Uses python3
import sys


class ItemValue:

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


class FractionalKnapSack:
    @staticmethod
    def get_optimal_value(capacity, weights, values):
        value = 0.
        initVal = []
        for i in range(len(weights)):
            initVal.append(ItemValue(weights[i], values[i], i))
        initVal.sort(reverse=True)
        for i in initVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity = capacity - curWt
                value = value + curVal
            else:
                fraction = capacity / curWt
                value += curVal * fraction
                capacity = int(capacity - (curWt * fraction))
                break
        return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = FractionalKnapSack.get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
