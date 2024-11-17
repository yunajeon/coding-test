def solution(s):
    a = ''
    s = sorted(s, reverse=True)
    for i in s:
        a += i
    return a