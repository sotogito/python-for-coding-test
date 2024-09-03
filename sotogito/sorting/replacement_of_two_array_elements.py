"""
목표 : A 배열의 합이 최대값이 되도록

풀이 : A배열의 최소값과 B배열의 최대값을 교환한다.

"""

n,k = map(int,input().split())

arrayA = list(map(int,input().split()))
arrayB = list(map(int,input().split()))

arrayA.sort()
arrayB.sort(reverse=True)

for i in range(k):
    #arrayA[i],arrayB[i] = arrayB[i],arrayA[i] # note 이것만 하면 만약 A 원소가 클 경우도 변경해버린다.

    if arrayA[i] < arrayB[i]:
        arrayA[i],arrayB[i] = arrayB[i],arrayA[i]
        continue


result = sum(arrayA)
print(result)


