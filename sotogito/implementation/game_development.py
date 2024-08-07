"""
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
-> 시계방향으로 먼저 회전해야됨
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 횐전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
-> 회전한 방향으로 위치를 옮겨야됨
-> 회전과, 회전한 방향으로 칸을 옮기는 것은 다른 동작임
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다


의문????????????????????????????????
뒤쪽 방향이 바다인 경우???
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
맵이 이거라면 0인 이동 가능한 땅은
(1,1)
(1,2)
(2,2)
인데
(1,1) -> (1,2)로 이동할떄 방향은 동쪽을 보고 진입인데..
그리고 (1,2) ->(2,2)이면 남쪽으로 보고 진입할텐데
결국은 뒤로 이동할떄가 되면 각각 동쪽, 남쪽을 바라볼테고, 지나왔던 방향으로 돌아갈수 있냐를 따지는거 아닌가? 그럼 결국은 뒤쪽이 방향인 경우가 있나?

그럼 결국 이동을 멈추는 경우는 뒤쪽 방향이 바다칸인 경우라 뒤로 이동할수 없는 경우가 아니라,
4면에 바다 and 이미 가본 땅일때 멈추는 거 같다. = 바다만 아

뒤쪽 방향이 바다칸인 경우라 뒤로 이동할수 없는 경우는 모든 면이 다 바다인 경우만 해당된다.
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


def is_move(nx, ny): #왼쪽으로 이동의 기준 : map 범위 안 && 육지인지 && 이미 가본 육지가 아닌지
    if 0 <= nx < len(game_map) and 0 <= ny < len(game_map[0]):
        if (game_map[nx][ny] == 0) and ((nx, ny) not in gone_land):
            return True
    return False

def is_game_continue(nx, ny):
        if (game_map[nx][ny] == 0):
            return True
        return False

while True:
    dir = (dir - 1) % 4     # note  현재 위치에서 현재 방향을 기준으로 왼쪽 방향    # note 4방향을 순환코드
    nx = x + dx[direction.index(dir)]   #note 방향 기준 왼쪽 위치를 구함 -> 차례대로 갈 곳을 정한다
    ny = y + dy[direction.index(dir)]


    if is_move(nx, ny):     #note 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면
        gone_land.append((x, y))    # 이미 가본 방향 저장
        x, y = nx, ny   # note 왼쪽으로 한 칸을 전진한다
        move_count += 1     # 움직임 업데이트
        not_move_count = 4  # 초기화

    elif not is_move(nx, ny):   #note 왼쪽 방향에 가보지 않은 칸이 없다면,
        not_move_count -= 1  # note 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.


    if not_move_count == 0:     # note 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는
        nx = x - dy[direction.index(dir)]
        ny = y - dx[direction.index(dir)]


        if game_map[nx][ny] == 0: #note 한 칸 뒤로 가고 1단계로 돌아간다.
            x, y = nx, ny
            not_move_count = 4
            continue

        break #note 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다


print(move_count)





