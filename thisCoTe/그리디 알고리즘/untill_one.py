'''
어떤 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
N과 K가 주어질 때, N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.
''' 
n, k = map(int, input().split())
cnt = 0

while n%k!=0:
  cnt += 1
  n -= 1

while n!=1:
  n //= k
  cnt += 1
print(cnt)

# 답안 예시 1
'''
# N, K를 공백을 기준으로 구분하여 입력받기
n, k = map(int, input().split())

result = 0

while True:
  # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
  target = (n // k) * k
  result += (n - target)
  n = target
  # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n<k:
    break
  # K로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
'''

# 답안 예시 2
'''
# N, K를 공백을 기준으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

whiel True:
  # N이 K로 나누어 떨어지는 수가 될 때까지 1씩 빼기
  target = (n//k) * k
  result += (n - target)
  n = target
  # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n<k:
    break
  # K로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)

'''