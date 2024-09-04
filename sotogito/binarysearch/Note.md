# 이진 탐색

### 순차 탐색
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서 부터 데이터를 하나씩 차례대로 확인하는 방법
- 데이터의 정렬 여부와 상관 없이 가장 앞에 있는 원소부터 확인한다.

### 이진 탐색
시작점+끝점+중간점 변수를 통해 찾으려는 데이터와 중간점 위치해 있는 데이터를 반복적으로 비교해 찾는 방법
- 데이터가 정렬이 되어 있어야 사용 가능하다.
- 정렬되어있는 상태에서 매우 빠르다.
- 탐색 범위를 정반씩 좁혀 나가며 데이터를 탐색하는 특징이 있다.
  - 한번 탐색할 떄마다 탐색할 원소의 개수가 절반씩 줄어든다.
- 구현 방법은 크게 재귀 & 반복문이 있다.
- 탐색 범위가 2,000만을 넘어가면 이진탐색을 고려한다.

#### 동작 방식
- 첫번째를 시작점으로 한다.
- 마지막을 끛점으로 한다.
- (시작점index+끝점index)//2 의 값을 중간점으로 한다.(소수점 버림)

- 데이터 < 중간점 : 중간점 이후 값을 볼 필요 없음 -> 끝점을 중간점-1 로 옮긴다.
- 데티터 > 중간점 : 중간점 이하 값을 볼 필요 없음 -> 시작점을 중간점을 옮긴다.
- 중간점의 값이 찾으려는 데이터가 될 때 탐색을 종료한다.

#### 예제 코드
- 공통 코드
```python
def binary_search(array, target, start, end):
  return "아래 구현해두었음"

# 원소 개수, 타겟 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재히지 않음")
else:
  print(result + 1)
```

- 반복문 사용
```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2  # 중간점 생성

        # 타겟을 찾은 경우
        if array[mid] == target:
            return mid
        # mid 이후를 볼 필요 없음 -> end 변경
        elif target < array[mid]:
            end = mid - 1
        # mid 이하 볼 필요 없음 -> start 변경
        elif target > array[mid]:
            start = mid + 1
    return None
```
- 재귀 사용  
반복문과 차이가 있다면 while문 대신에  재귀 탈출 조건을 추가한 것이다.
```python
def binary_search(array, target, start, end):
    if start > end: 
        return None
    mid = (start + end) // 2
    
    # 타겟을 찾은 경우
    if array[mid] == target:
        return mid
    # mid 이후를 볼 필요 없음 -> end 변경
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    # mid 이하 볼 필요 없음 -> start 변경
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, end)

```

---
## 이진 탐색 트리 Binary Search Tree, BST
- 입력 데이터가 많거나 탐색 번위가 매우 넓은 편이다.
트리를 사용하면 이진탐색과 같은 탐색 기법이 빠르다.
```text
          A          <- 루트 노드 (Root Node) : 최상단 노드
         / \
        /   \
       B     C       <- B, C는 서브트리의 루트 : [B-D-E],[C-F-G-H]
      / \   / \
     D   E F   G     <- 서브트리의 내부 노드 (Subtree Internal Nodes)
                \
                 H   <- 단말 노드 (Leaf Node) : 최하단 노드
```
모든 트리가 이진 탐색 트리는 아니다.  
다양한 형태의 트리가 있는데, 이진 탐색 트리만이 이진 탐색을 수행할 수 있는 규칙을 따른다.  
( 자바 TreeMap, TreeSet이 바로 이 이진탐색트리다!!)
- 일반적인 트리
```text
      5
     / \
    3   7
   / \
  8   2 
```
- 이진 탐색 트리
```text
      5
     / \
    3   7
   / \
  2   4       왼쪽값이 가장 작음
```
    왼쪽 자식 노드 < 부모 노드 < 왼쪽 자식 노드

- 루트 노드 < 타겟 : 왼쪽(작은) 트리 버림
- 루트 노드 > 타겟 : 오른쪽(큰) 트리 버림
---
#### 빠른 입력받기 - sys
```python
import sys
input_data = sys.stdin.readline().rstrip()
```