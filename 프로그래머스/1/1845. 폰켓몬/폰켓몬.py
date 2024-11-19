def solution(nums):
    answer = 0
    mon_type = {}
    
    for i in nums:
        if i not in mon_type:
            mon_type[i] = 1
        else:
            mon_type[i] += 1
            
    if len(mon_type) >= len(nums)/2:
        return len(nums)/2
    else: return len(mon_type)