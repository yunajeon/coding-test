from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

# 중복 순열
'''
from itertools import product

data = ['A', 'B', 'C']

result = list(product(data, repeat=2))
print(result
'''