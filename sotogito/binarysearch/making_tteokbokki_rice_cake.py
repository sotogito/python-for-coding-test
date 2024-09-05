"""
H 보다 길어야 짤림, 짧으면안짤림
예를들어 15 14 10 17 이고 절단기 H 가 15면
15 14 10 17 이 됨.
0 + 0 + 0 + 2 = 총 2cm

N : 떡의 개수
M : EJrdml rlfdl

1. 떡보다 길이가 작아야됨 - 요구 숫자가 0이 아닌 이
0부터 ~ max까지?
"""
"""
n,m = map(int,input().split())
array = list(map(int,input().split()))

height_list = []
for i in range(max(array)):
    height_list.append(i)

for h in height_list:
    result = 0
    for a in array:
        if a > h:
            result += (a-h)
        else:
            continue

    if result == m:
        print(h)
"""

"""
파라메트릭 서치 문제

1. 0~max(array)까지의 배열을 만든다.
2. 시작점, 중간점, 끝점을 설정한다.


- mid값으로 계산한 값 > target : mid값 이하 값 버림
- mid값으로 계싼한 값 < target : mid 이후 값 버림 
-> target이 작고 떡 크기와 차이가 많이 날수록 값이 큼


- 종료 조건 : mid 값으로 계산했을 때 타겟 값이 나오는 경우
"""
n,m = map(int,input().split())
array = list(map(int,input().split()))

height_list = []
for i in range(max(array)):
    height_list.append(i)

array.sort()


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    mid_target = get_target(array[mid])

    if mid_target == target:
        return array[mid]

    elif mid_target > target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)



def get_target(h):
    result = 0
    for i in array:
        if i > h:
            result += (i-h)

    return result


result = binary_search(array, m, 0, n-1)
if result == None:
    print(-1)
else:
    print(result)