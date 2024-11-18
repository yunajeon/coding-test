def solution(t, p):
    answer = 0

    for i in range(len(t)-len(p)+1):
        new_t = t[i:i+len(p)]
        if int(new_t) == int(p) or int(new_t) < int(p):
            answer += 1
    '''
    left = 0
    right = p_len
    while right < len(t)+2:
        new_t = t[left:right]
        if int(new_t) == int(p) or int(new_t) < int(p):
            answer += 1
        left += 1
        right += 1
        '''
    return answer