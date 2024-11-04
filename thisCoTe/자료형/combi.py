from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result)

# 중복 조합
'''
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))
print(result)
'''