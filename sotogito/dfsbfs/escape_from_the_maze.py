"""
위치 : (1,1)
출구 : (N,M)

0 : 괴물이 있는 곳
1 : 괴물이 없는 곳

움직여야하는 최소 칸의 개수


음료수 얼려 먹기 문제와 다른점이 있다면 좌표값이 1인 곳으로 목표지점까ㅣㅈ 최소한으로 운직여야한다는 것이다.
음료수 열러먹기의 경우애는 좌표값이 상하좌우로 0인부분일떄까지 재귀로 찾아내면 됐었다./.
"""
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 미로 범위를 벗어나면 무시
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue

            # 벽이거나 이미 방문한 경우 무시
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

shortest_path = bfs(1, 1)
print(shortest_path)