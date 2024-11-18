def solution(arr1, arr2):
    answer = []
    for a1,a2 in zip(arr1, arr2):
        result = []
        for i in range(len(arr1[0])):
            result.append(a1[i]+a2[i])
        answer.append(result)
    return answer