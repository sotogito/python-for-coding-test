# 최단 경로
- 다익스트라 알고리즘 (Dijkstra's Algorithm)
- 플로이드-워셜 알고리즘 (Floyd-Warshall Algorithm)
- 벨만-포드 알고리즘 (Bellman-Ford Algorithm)

## 1. 다익스트라 알고리즘
그래프에 여러개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘  
각 노드에 대한 현재까지의 최단 거리 정보를 1차원 리스트에 저장하며 계속 갱신한다.


1. 시작 점을 0으로 설정하고 탐색하지 않은 노드값을 무한으로 설정한다.
2. 연결된, 탐색하지 않은 노드의 결로를 계산하고 최소값을 업데이트한다.
4. 연결된 노드의 탐색을 모두 마쳤다면 가장 작은 노드로 이동한다.
5. 1~4번을 반복한다.

#### 예시 플로우
```text
     A
    / \
   1   4
  /     \
 B---2---C
  \     /
   5   1
    \ /
     D

```
A -> B = 1  
A -> C = 4

       [A: 0, B: 1, C:4 , D: ∞]
 
B -> C : 1(B의 최단 경로) + 2 = 3   *C 의 최단 경로 갱신
B -> D : 1(B의 최단 경로) + 5 = 6

        [A: 0, B: 1, C:3 , D: 6]

C -> D : 3(C의 최단 경로) + 1 = 4    *D 의 최단 경로 갱신

    [A: 0, B: 1, C:3 , D: 4]


- ???? B와 C 노드중 어떤 것이 먼저 탐색을 할까  
-> 현재 노드의 최단 경로가 작은 값부터 탐색을 시작한다.  
  
---
## 힙 Heap
힙 자료구조를 이용하게 되면 최단 경로를 더 빠르게 찾을 수 있다.  
큐를 구현하기 위해 사용하는 자료구조 중 하나다. - 선입선출

| 자료구조   | 추출되는 데이터              | 
|--------|-----------------------|
| 스택     | 가장 최근에 삽인된 데이터 - 후입선출 | 
| 큐      | 가장 먼저 삽인된 데이터 - 선입선출  | 
| 우선순위 큐 | 가장 우선순위가 높은 데이터       | 

- `PriorityQueue`
- `heapq` : 더 빠르게 동작
  - heappush: 우선순위 큐에 요소를 추가
  - heappop: 우선순위 큐에서 가장 작은 요소를 꺼냄
  - heapify: 리스트를 힙 구조로 변환

```python
import heapq

priority_queue = []
heapq.heappush(priority_queue, 3)
print(heapq.heappop(priority_queue))  # 1

max_heap = []
heapq.heappush(max_heap, -3)

# 기존 리스트
nums = [5, 1, 3, 7, 2, 8]
heapq.heapify(nums)
# 리스트를 최대 힙으로 변환 (음수로 변환 후 heapify)
nums = [-num for num in nums]
heapq.heapify(nums)
```
- 최소 힙 : 기본적으로 제공
- 최대 힙 : 음수를 붙임  

## 다익스트라 + 힙
- 최소 거리를 갱신해서 다시 저장할 필요 없다. -> _노드의 가장 먼저 pop되는 값이 어차피 최소이기 떄문_
- 다음 담색 노드(최소 거리)를 구할 필요 없다.  -> _최소 힙으로 꺼내 쓰기 떄문_

다익스트라 알고리즘 에서는 최소힙을 사용한다.  
우선순위 큐에는 다음과 같은 객체를 담는다. 정렬은 x값을 기준으로 한다.

    (거리:x,노드:y) (거리:x,노드:y) (거리:x,노드:y)
작은 순대로 꺼내지기 때문에 배열의 최소값을 구할 필요 없이 그냥 꺼내기만 하면 된다.  
꺼낸 뒤 해당 노드를 이미 처리한 적 있는지만 확인한다.


#### 배열과 힙 사용의 차이점
- 배열 : 최소 거리가 갱신되면 배열의 값을 최소값으로 변경한다.
- 힙 : 일단 데이터를 넣고 나중에 꺼낼때, 노드의 가장 먼저 빠진 값을 최소값으로 한다. - 최소 힙이기 떄문  
1. 노드 2의 거리가 4임 (거리:4,노드2)
2. 노드 2의 거리가 2로 갱신됨 (거리:2,노드2)  
이떄의 큐를 확인하면 다음과 같다.

        (거리:2,노드2) (거리:4,노드2)

그리고 꺼낼때 노드 2의 값은 최소값인 2가 먼저 빠진다. 추후 빠지는 노드 2의 값은 최소값이 아니기 때문에 무시해도 된다.  


- 개선된 다익스트라 알고리즘 소스 코드

```python
import heapq

INF = int(1e9)  # 최단 거리를 무한으로 초기화함

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]  # 각 노드와 간선의 데이터
distance = [INF] * (n + 1)  # 최종 최단 거리를 저장하는 배열

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())  # 노드 a,b의 간선 길이 c
    graph[a].append((b, c))


def dijkstra(start):
    q = []

    # 시작 노드 0으로 설정
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # q가 비어있지 않을동안 탐색 (distance에 모두 등록되었을 때 멈춤)
    while q:
        dist, now = heapq.heappop(q)  # 가장 최단거리 pop (거리-노드)

        # 노드가 이미 distance에 등록 되었다면 pass
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 노드 탐색
        for near in graph[now]:  # graph[now] : 현재 노드 / i : (인접 노드, 거리)
            cost = dist + near[1]  # 현재 노드의 거리 + 인접 노드의 거리

            # 최단 거리가 갱신된 경우
            if cost < distance[near[0]]:
                distance[near[0]] = cost  # 해당 노드 최단 거리 갱신
                heapq.heappush(q, (cost, near[0]))


dijkstra(start)

# 결과 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
```
---
### 다익스트라 vs 플로이드 워셜
- 다 익스트라
  - 하나의 시작 노드에서 다른 모든 노드까지의 최단 경로를 구한다.
  - _**단일**_ 출발점 최단 경로 문제를 해결
- 플로이드 워셜
  - 모든 노드 간의 최단 경로를 구함
  - 모든 _**쌍**_! 최단 경로 문제를 해결

---
## 2. 플로이드 워셜 알고리즘
모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우 사용하는 알고리즘  
플로이드 워셜의 가장 큰 특징은 거리를 노드 쌍으로 저장하다는 것이다.  
때문에 다익스트라와 다르게 이중배열이 사용된다.  
```text
      2
  1 -----> 2
  |        |
 4|        |1
  |        v
  3 <----- 4
      3

```
|      | 1   | 2   | 3   | 4   |
|------|-----|-----|-----|-----|
| **1** | 0   | 2   | 4   | INF |
| **2** | INF | 0   | INF | 1   |
| **3** | INF | INF | 0   | INF |
| **4** | INF | INF | 3   | 0   |
 distance[세로][가로]  

위에는 초기화 해준 이중 배열 그래프의 형태이다.  
같은 노드에서는 이동 거리가 없기 떄문에 0으로 초기화 해준다.  
기본 노드간의 거리 또한 초기화 해준다.  

_???? [2][1]하고 [1][2]하고 데이터가 다를까? 결국 지나가는 데이터는 똑같은데?  
-> 그래프가 유향(방향이 있는) 그래프의 경우는 다를 수 있다_
- 거리 탐색

k : 중간 노드  
i : 출발 노드  
j : 도착 노드  
중간노드를 설정하고, 모든 노드 쌍(i,j)에 대해 경로를 비교한다.  
- `i -> k -> j` (거쳐감)  distance[i][k] + distance[k][j]
- `i -> j`(바로감) distance[i][j]
```python
for k in range(1, n + 1):  # 중간 노드 k
    for i in range(1, n + 1):  # 출발 노드 i
        for j in range(1, n + 1):  # 도착 노드 j
          
            # i에서 j로 가는 기존 거리와 i -> k -> j로 가는 경로의 거리 비교하여 최단 거리 갱신
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
```

_????? 반복문의 중첩의 순서를 변경하면 어떻게될까?   
-> 안된다. 중간노드는 모든 노드가 한번씩 거쳐가야하므로 가장 바깥쪽 루프에 둔다.  
중간 노드를 고정하고 (시작->끝) 노드 for문을 돌리는 것이 바람직하다._

```python
INF = int(1e9)

n = int(input())
m = int(input())

# 2차원 그래프
graph = [[INF] * (n+1) for i in range(n+1)] # index를 1부터 시작

# 자기 자신 최단 거리 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 기본 간선 간의 거리 초기화 - [시작,끝,거리] 입력 받음
for _ in range(m):
    a,b,c = map(int, input().split()) # start, end, length
    graph[a][b] = c


# 최단 거리 탐색 및 graph 업데이트
for middle in range(1,n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end],graph[start][middle]+graph[middle][end])


# 결과 출력
for start in range(1, n+1):
    for end in range(1, n+1):
        if graph[start][end] == INF:
            print("INF",end= " ") # 배열의 행이 출력되기 때문에 end로 데이터를 구분함
        else:
            print(graph[start][end],end= " ")
    print() # 줄바꿈
        
        
```