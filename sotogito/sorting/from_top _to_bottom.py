n = int(input())

array = []
for i in range(n):
    array.append(int(input()))


# note 정렬 라이브러리
# array.sort(reverse=True)

#note 선택 정렬
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if array[j] > array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(*array)
