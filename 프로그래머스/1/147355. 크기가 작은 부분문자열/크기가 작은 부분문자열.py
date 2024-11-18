def solution(t, p):
    answer = 0
    p_len = len(p)
    left = 0
    right = p_len
    while right <= len(t):
        new_t = t[left:right]
        if int(new_t) == int(p) or int(new_t) < int(p):
            answer += 1
        left += 1
        right += 1

    return answer