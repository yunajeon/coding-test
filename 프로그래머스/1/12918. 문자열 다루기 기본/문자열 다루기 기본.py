def solution(s):
    try:
        if (len(s) == 4 or len(s) == 6) and (int(s) or int(s) == 0):
            return True
        else:
            return False
    except:
        return False