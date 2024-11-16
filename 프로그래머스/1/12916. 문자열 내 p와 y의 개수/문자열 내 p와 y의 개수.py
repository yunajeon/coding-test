def solution(s):
    s = s.lower()
    if (s.count('p') == s.count('y')) or ('p' not in s and 'y' not in s):
        return True
    else:
        return False
    