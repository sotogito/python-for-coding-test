"""
1. 8 * 8
2. 나이트는 밖으로 나갈 수 없음
3. 수평 2 + 수직 1 / horizontal[i+2] + vertical[i+1]
4. 수직 1 + 수평 2 / horizontal[i+1] + vertical[i+2]

나이트의 위치가 주어질 때 움직일 수 있는 경우의수
"""

horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertical = ['1', '2', '3', '4', '5', '6', '7', '8']

steps = [(-2, -1), (-1, -2), (2, -1), (1, -2), (-1, 2), (-2, 1), (1, 2), (2, 1)]

input_data = input()

hor = input_data[0]
ver = input_data[1]

hor_index = horizontal.index(hor)
ver_index = vertical.index(ver)

count = 0

for step in steps:
    hor_step = hor_index + step[0]
    ver_step = ver_index + step[1]
    if(hor_step >= 0 and hor_step <= len(horizontal) and ver_step >= 0 and ver_step <= len(vertical)):
        count += 1

print(count)