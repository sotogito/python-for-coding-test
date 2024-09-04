"""
N : 매장의 부품 개수
M : 손님의 부품 개수


"""
import sys

# note 입력
n = int(input())
arrayN = sys.stdin.readline().split()

M = int(input())
arrayM = sys.stdin.readline().split()


# note 구현
arrayN.sort()
arrayM.sort()

def dinart(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return dinart(array, target, start, mid -1)
    elif array[mid] < target:
        return dinart(array, target, mid + 1, end)


result_array = []

for dataM in arrayM:
    result = dinart(arrayN, dataM, 0, n - 1)
    if result == None:
        result_array.append("no")
    else:
        result_array.append("yes")

print(*result_array)