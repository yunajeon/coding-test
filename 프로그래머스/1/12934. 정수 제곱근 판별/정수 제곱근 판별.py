import math

def solution(n):
    x = int(math.sqrt(n))
    if n == x*x:
        return math.pow(x+1, 2)
    else:
        return -1