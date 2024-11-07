'''
다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 m번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없음
-> n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 최대 연속 가능한 수
'''
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort() # data 오름차순 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수
result = 0

while True:
  for i in range(k): # 가장 큰 수를 k번 더하기
    if m == 0: # m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1 # 더할 때마다 1씩 빼기
  if m == 0:
    break
  result += second # 두 번째로 큰 수 한 번 더하기
  m -= 1

print(result)

# 답안 예시
'''
# N, M, K를 공백을 기준으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)
'''