a, b = map(int, input().strip().split(' '))
result = ""
for _ in range(b):
    for _ in range(a):
        result += "*"
    result += "\n"
print(result)