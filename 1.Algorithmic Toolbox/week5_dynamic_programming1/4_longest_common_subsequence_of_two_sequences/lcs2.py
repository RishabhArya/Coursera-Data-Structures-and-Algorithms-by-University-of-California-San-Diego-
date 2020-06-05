# python3
import numpy
import sys

def LCS2(s1, s2, n1, n2):
    """ Finds the length of the longest common subsequence of two strings
    (str, str, int, int) -> (int, 2D-array) """

    # Initializing the matrix
    Matrix = numpy.zeros((n1 + 1, n2 + 1))

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                Matrix[i][j] = Matrix[i - 1][j - 1] + 1
            if s1[i - 1] != s2[j - 1]:
                Matrix[i][j] = max(Matrix[i][j - 1], Matrix[i - 1][j])

    return (int(Matrix[n1][n2]), Matrix)


if __name__ == '__main__':

    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n1 = data[0]
    data = data[1:]
    s1 = data[:n1]

    data = data[n1:]
    n2 = data[0]
    data = data[1:]
    s2 = data[:n2]
    LCS_length, Matrix = LCS2(s1, s2, n1, n2)
    print(LCS_length)
