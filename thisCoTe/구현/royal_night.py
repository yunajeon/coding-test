'''
8 * 8 좌표 평면에서 나이트는 현재 위치에서 L자 형태로만 이동 가능
& 정원 밖으로 나갈 수 없다.
< 이동할 수 있는 방향 >
- 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
- 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
'''
s = input()
count = 0

if '1' or '8' in s:
    if 'a' or 'h' in s:
        count = 2
    elif 'b' or 'g' in s:
        count = 3
    else:
        count = 4
elif '2' or '7' in s:
    if 'a' or 'h' in s:
        count = 3
    elif 'b' or 'g' in s:
        count = 4
    else:
        count = 6
else:
    if 'a' or 'h' in s:
        count = 4
    elif 'b' or 'g' in s:
        count = 6
    else:
        count = 8

print(count)

# 답안 예시
'''
- 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동 가능한지 확인
  -> 리스트를 이용하여 8가지 방향에 대한 방향 벡터 정의
'''
'''
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
'''