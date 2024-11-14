def solution(a, b):
    return sum(list(i for i in range(min(a, b), max(a, b)+1)))