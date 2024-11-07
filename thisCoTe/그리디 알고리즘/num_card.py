'''
각 행에서 숫자가 가장 낮은 카드들 중 가장 큰 수
'''
n, m = map(int, input().split())

min_data = 0

for i in range(n):
  data = list(map(int, input().split()))
  if min_data<min(data):
    min_data = min(data)

print(min_data)

# 답안 예시1 -> min 함수 이용
'''
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)
'''

# 답안 예시2 -> 2중 반복문 구조 이용
'''
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
    result = max(result, min_value)

print(result)
'''