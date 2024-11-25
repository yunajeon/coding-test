def solution(n):
    answer = []
    result = 0
    k = 0
    
    while not (n >= 3**k and n < 3**(k+1)):
        k += 1

    for i in range(k, -1, -1):
        j = 3**i
        answer.append(n//j)
        n -= ((n//j)*j)
        
    for i in range(k+1):
        result += (answer[i]*(3**i))
    
    return result