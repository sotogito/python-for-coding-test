"""
- 왼쪽으로 회전
- 왼쪽에 가보지 않은 칸 : 왼쪽 회전 - 이동
- 왼쪽에 가본 칸 : 왼쪽 회전만

- 4면이 모두 가본칸이거나 or 바다일 경우 -> 뒤로 한칸(바다이면 이동 못함)

1. 왼쪽 확인,
"""

direction = [3, 2, 1, 0]  #서, 남, 동, 북
left_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
front_direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
back_direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]

already_been_to = []

land = 0
sea = 1
game_map = []

h, v = map(int, input().split())
hor, ver, dir = map(int, input().split())  #가로 세로 방향
for i in range(h):
    one_line = list(map(int, input().split()))
    game_map.append(one_line)

user_location = [hor, ver]
user_direction = dir
move = 1
can_not_move_count_down = 4

while True:
    already_been_to.append([user_location[0], user_location[1]])
    left_direction_index = direction.index(user_direction)
    #next_direction_index = (direction_index + 1) % len(direction)
    #left_direction_index = direction.index(user_direction)
    left_value = left_direction[left_direction_index]

    next_x = user_location[0] + left_value[0]
    next_y = user_location[1] + left_value[1]

    is_move = True
    if (0 <= next_x < h and 0 <= next_y < v and
            (game_map[next_x][next_y] == sea or [next_x, next_y] in already_been_to)):
        is_move = False

    if can_not_move_count_down == 0:
        back_direction_index = direction.index(user_direction)
        back_value = back_direction[back_direction_index]
        user_location = [user_location[0] + back_value[0], user_location[1] + back_value[1]]
        next_x = user_location[0] + back_value[0]
        next_y = user_location[1] + back_value[1]

        is_move = True
        if (0 <= next_x < h and 0 <= next_y < v and
                (game_map[next_x][next_y] == sea or [next_x, next_y] in already_been_to)):
            is_move = False

        if not is_move:
            break

    if is_move:  #움직일 수 있으면
        user_direction = direction[(direction.index(user_direction) + 1) % len(direction)]
        front_direction_index = direction.index(user_direction)  #전진하 계산 Index 가져오고
        front_value = front_direction[front_direction_index]
        next_x = user_location[0] + front_value[0]
        next_y = user_location[1] + front_value[1]



        user_location = [user_location[0] + front_value[0], user_location[1] + front_value[1]]
        can_not_move_count_down = 4
        move += 1
        continue
    elif not is_move:
        user_direction = direction[(direction.index(user_direction) + 1) % len(direction)]
        can_not_move_count_down -= 1
        continue

print(move)
