import sys

def m_construction(text):
    n = len(text)
    new_text = text * 2
    return [new_text[i:i+n] for i in range(n)]


def m_construction_sorted(text):
    return sorted(m_construction(text))


def bwt_construction(text):
    n = len(text)
    M = m_construction_sorted(text)
    return M[0]



if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    print(bwt_construction(text))