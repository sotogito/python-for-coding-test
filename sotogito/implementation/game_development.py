"""
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
-> 시계방향으로 먼저 회전해야됨
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 횐전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
-> 회전한 방향으로 위치를 옮겨야됨
-> 회전과, 회전한 방향으로 칸을 옮기는 것은 다른 동작임
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다



"""

map_h, map_v = map(int, input().split())
x, y, dir = map(int, input().split())  # 가로 세로 방향
game_map = []
for i in range(map_h):
    one_line = list(map(int, input().split()))
    game_map.append(one_line)



gone_land = []
direction = [0, 3, 2, 1]  # 왼쪽으로 회전 순 -> 북 서 남 동
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


move_count = 1
not_move_count = 4


def is_move(nx, ny):
    if 0 <= nx < len(game_map) and 0 <= ny < len(game_map[0]):
        if (game_map[nx][ny] == 0) and ((nx, ny) not in gone_land):
            return True
    return False

def is_game_continue(nx, ny):
    if 0 <= nx < len(game_map) and 0 <= ny < len(game_map[0]):
        if (game_map[nx][ny] == 0):
            return True
    return False


while True:
    dir = (dir - 1) % 4  # note 4방향을 순환코드
    nx = x + dx[direction.index(dir)]
    ny = y + dy[direction.index(dir)]


    if is_move(nx, ny):
        gone_land.append((x, y))
        x, y = nx, ny
        move_count += 1
        not_move_count = 4

    elif not is_move(nx, ny):
        not_move_count -= 1


    if not_move_count == 0:
        back_index = (dir + 1) % 4
        nx = x - dx[direction.index(back_index)] # 1,0 / 2.1 / 1.2 / 0.1 동 : +1 0
        ny = y - dy[direction.index(back_index)]

        if is_game_continue(nx, ny):
            x, y = nx, ny
            move_count += 1
            not_move_count = 4
            continue
        else:
            break


print(move_count)












"""

map_h, map_v = map(int, input().split())
x, y, dir = map(int, input().split())  # 초기 위치와 방향
game_map = []
for i in range(map_h):
    one_line = list(map(int, input().split()))
    game_map.append(one_line)

# 방향은 북, 동, 남, 서 순서로 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * map_v for _ in range(map_h)]
visited[x][y] = True

move_count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    dir = (dir - 1) % 4
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하고, 바다가 아닌 경우 이동
    if not visited[nx][ny] and game_map[nx][ny] == 0:
        x, y = nx, ny
        visited[x][y] = True
        move_count += 1
        turn_time = 0
        continue
    else:  # 이동할 수 없는 경우
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤로 갈 수 있다면 이동
        if game_map[nx][ny] == 0:
            x, y = nx, ny
        else:  # 뒤가 바다로 막혀있는 경우
            break
        turn_time = 0

print(move_count)

"""