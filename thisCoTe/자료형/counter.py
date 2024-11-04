from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # blue 개수
print(counter['green']) # green 개수
print(dict(counter)) # 사전형 자료형으로 반환