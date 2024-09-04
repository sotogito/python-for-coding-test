"""
H 보다 길어야 짤림, 짧으면안짤림
예를들어 15 14 10 17 이고 절단기 H 가 15면
15 14 10 17 이 됨.
0 + 0 + 0 + 2 = 총 2cm

N : 떡의 개수
M : EJrdml rlfdl

1. 떡보다 길이가 작아야됨 - 요구 숫자가 0이 아닌 이상


0부터 ~ max까지?

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