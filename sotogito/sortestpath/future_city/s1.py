"""
A : 방문 판매원
1~N : 미래도시
k : 중간 도착 소개팅
X : 최종 도착 회사

최단경로 구한다음에
graph[시작][소개팅]+graph[소개팅][회사]

간선간의 길이는 기본 1이므로 굳이 최단길이를 저장할 필요가 있을끼 싶은데

내가 구해야할것 :
1 -> K -> X
로 가는데 다른 도시를 지나쳐야하는 지.
만약 중간에 다름 도시를 지나야한다면?

k와 x가 아닌 다른 노드는 그냥 거리로 합쳐버리된 되지 않을까
예를들어서 k사이에 다른 도시가 있다면 그걸 1+(중간 도시 개수)로해서 최단거리를 구하면?

그럼 플로이드보다는 다익스트라가 맞나

"""
import heapq

INF = int(1e9)

n,m = map(int,input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e,1)

x,k = map(int,input().split())

middle = False #K
end = False #x
count = 0
def dijkstra(start):
    q = []

    heapq.heappush(q,(0,1))
    distance[1] = 0

    while True:
        if middle == True and end == True:
            break

        dist, now = heapq.heappop(q)

        for near in graph[now]:
            node = near[0]
            cost = dist + near[1]

            if middle == False and node != k:
                distance[node] = cost
                heapq.heappush(q,(cost,node))









