'''
왼쪽부터 하나씩 모든 숫자를 확인하며 숫자 사이에 '*' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성해라.
모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정.
'''
data = input()

result = int(data[0])

for i in range(1, len(data)):
  if (result+int(data[i]) > result*int(data[i])):
    result = result + int(data[i])
  else:
    result = result * int(data[i])

print(result)

# 문제 답
'''
# 두 수에 대해 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 "+", 그렇지 않은 경우에는 "*" 연산자를 사용한다.

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
  # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)
'''