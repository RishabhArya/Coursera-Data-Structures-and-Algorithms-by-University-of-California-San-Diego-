# python3


class HeapBuilder:
    def __init__(self):
        self.swaps = []
        self.array = []

    @property
    def size(self):
        return len(self.array)

    def read_data(self):
        n = int(input())
        self.array = [int(s) for s in input().split()]
        assert n == self.size

    def write_response(self):
        print(len(self.swaps))
        for swap in self.swaps:
            print(swap[0], swap[1])

    def l_child_index(self, index):
        l_child_index = 2 * index + 1
        if l_child_index >= self.size:
            return -1
        return l_child_index

    def r_child_index(self, index):
        r_child_index = 2 * index + 2
        if r_child_index >= self.size:
            return -1
        return r_child_index

    def sift_down(self, i):
        min_index = i
        l = self.l_child_index(i)
        r = self.r_child_index(i)

        if l != -1 and self.array[l] < self.array[min_index]:
            min_index = l

        if r != - 1 and self.array[r] < self.array[min_index]:
            min_index = r

        if i != min_index:
            self.swaps.append((i, min_index))
            self.array[i], self.array[min_index] = \
                self.array[min_index], self.array[i]
            self.sift_down(min_index)

    def generate_swaps(self):
        for i in range(self.size // 2, -1, -1):
            self.sift_down(i)

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == "__main__":
    heap_builder = HeapBuilder()
    heap_builder.solve()
