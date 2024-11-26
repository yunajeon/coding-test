def solution(s):
    answer = []
    dict_s = dict()
    
    for i in range(len(s)):
        if s[i] in dict_s:
            dict_si = dict_s[s[i]]
            answer.append(i-dict_si[-1])
            dict_s[s[i]].append(i)
        else:
            dict_s[s[i]] = [i]
            answer.append(-1)
    return answer