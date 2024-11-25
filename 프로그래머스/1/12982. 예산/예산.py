def solution(d, budget):
    answer = len(d)
    d = sorted(d, reverse = True)
    print(d)
    total = sum(d)
    if total <= budget:
        return answer
    else:
        for i in d:
            total -= i
            answer -= 1
            if total <= budget:
                return answer