import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        num = self.n = int(sys.stdin.readline())
        if num == 0:
          print("CORRECT")
          exit()
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        self.inOrderTraversal(0)
        return self.result

    def inOrderTraversal(self, index):
        if self.left[index] != -1:
            self.inOrderTraversal(self.left[index])
        self.result.append(self.key[index])
        if self.right[index] != -1:
            self.inOrderTraversal(self.right[index])

def checkBst(arr):
  for x in range(len(arr) - 1):
    if arr[x + 1] < arr[x]:
      return False

  return True

def main():
    tree = TreeOrders()
    tree.read()
    arr = tree.inOrder()
    if checkBst(arr):
      print("CORRECT")
    else:
      print("INCORRECT")

threading.Thread(target=main).start()