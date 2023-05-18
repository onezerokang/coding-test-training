import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b, m_cnt1, m_cnt2):
    if (a * m_cnt1) == (b * m_cnt2):
        return a * m_cnt1
    if (a * m_cnt1) > (b * m_cnt2):
        return lcm(a, b, m_cnt1, m_cnt2 + 1)
    else:
        return lcm(a, b, m_cnt1 + 1, m_cnt2)

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b, 1, 1))