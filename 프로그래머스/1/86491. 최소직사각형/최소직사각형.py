import numpy as np
def solution(sizes):
    npsizes = np.array(sizes)
    max_w = 0
    max_h = 0
    for w, h in sizes:
        width = max(w, h)
        height = min(w, h)
        max_w = max(max_w, width)
        max_h = max(max_h, height)
    return max_w*max_h