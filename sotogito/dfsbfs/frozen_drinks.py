n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input()))) #note 공백 없이 받기 떄문에 split() 이 필요 없음
    #graph.append(list(map(int, input().split()))) 이건 왜 안되지


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: # 벗어날 경우, index가 0보다 작거나 n,m보다 같거나 크면 안됨
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 #note 이미 방문한 좌표를 1로 변경하여 재귀를 막음

        # note 각각 재귀로 상하좌우가 0이면 계속 재귀로 돌고 벗어나는 조건에서 ture를 반환하여 count함
        # note 즉 아래 재귀는 0이 아닐떄까지 하게됨
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    return False # note 좌표값이 1일 경우는 재귀를 돌지 않음


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)
