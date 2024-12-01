def solution(x):
    hassard_n = sum(list(map(int, list(str(x)))))
    return x%hassard_n == 0