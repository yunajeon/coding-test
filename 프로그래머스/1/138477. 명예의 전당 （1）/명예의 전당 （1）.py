def solution(k, score):
    answer = []
    hof = []
    
    for i in score:
        if len(hof) >= k and i > min(hof):
            hof.remove(min(hof))
            hof.append(i)
        elif len(hof) < k:
            hof. append(i)
        answer.append(min(hof))
    return answer