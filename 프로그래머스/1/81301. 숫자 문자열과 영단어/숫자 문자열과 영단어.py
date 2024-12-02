def solution(s):
    answer = ''
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    find_num = ''
    
    for i in s:
        if i.isdigit():
            answer += i
        else:
            find_num += i
            if find_num in num_list:
                answer += str(num_list.index(find_num))
                find_num = ''
    return int(answer)