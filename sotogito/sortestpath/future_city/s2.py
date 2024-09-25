"""
왜 !!1 독립적으로 생ㄱ가하지ㅏ 못했을까ㅣ??????????????ㅇㄴㅇㄴㅇㄴㅇㄴㅇ
특히 플로이드 워셜로 풀면 각자 노드간의 '독립적인 거리'를 기록하기 떄문에!!ㅡㅜ\
그냥 [start-중간 소개팅]+[소개팅+마지막 도시] 최단거리를 더해주기만하면 된다..
"""

INF = int(1e9)

n,m = map(int,input().split())
graph = [[INF] * (n+1) for i in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
for _ in range(m):
    a,b = map(int, input().split()) # start, end, length
    graph[a][b] = 1
    graph[b][a] = 1 #note

x,k = map(int,input().split()) #끝,중간


for middle in range(1,n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end],graph[start][middle]+graph[middle][end])


result = graph[1][k]+graph[k][x]

if result % INF == 0: #note 만약 INF+INF 상황도 있을 수 있기 때문에 나머지를 확인
    print(-1)
else:
    print(result)