"""
일직선상 최소 한칸 이상 떨어진 숫자를 조합해 최대값을 구해야함

1. 인덱스 + 숫자 순으로 저장하고 정렬함

가장 큰 숫자부터 먹는데 막약 인덱스의 차이가 1 이하면 먹으면 안됨
먹은 인딕스 저장하기
새로 먹을 숫자가
현재 숫자와 1이상이 차이나고 and 인덱스 리스트에 1 이상 차이나는지 확인하기

문제 1.
1 11 15 12 2
만약 이럴 경우 내 로직대로라면 15를 먹고 2, 1을 먹어서 최종 18이 된다.
하지만 사실 가장 큰 최대값을 어딕 위해서는 11+12를 먹어야한다.

즉, 최대값을 기준으로 먹이를 먹는게 아니라, 결국 최종적인 최대값이 커야한다.

문제 2.
1 15 11 12 40

일단 40을 먹어야하는건 확실하다.
내 로직대로라면 1 + 11+40 = 52가 나와야한다.
하지만 실제로 큰 수는 40+15이다. 55로 더 큰 수가 나온다.



1 : 1+ 15+2 = 18
11 : 11+12

"""

n = int(input())
array = list(map(int, input().split()))
food = []
for i in range(n):
    food.append((i, array[i]))
eat = []

result = 0

food.sort(key=lambda x: x[1], reverse=True)



eat.append(-1)

for i in range(n-1):
    now = food[i][0]
    next = food[i+1][0]


    if abs(now - next) >= 1:
        count = 0
        for e in eat:
            if abs(e-now) <= 1:
                count += 1

        if count == 0:
            result += food[i][1]
            print(food[i][1])
            eat.append(now)


print(result)