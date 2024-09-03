n = int(input())
students = []

for i in range(n):
    student = input().split()
    students.append(student)

# note 선택정렬
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if students[min_index][1] > students[j][1]:
            min_index = j

    students[i], students[min_index] = students[min_index], students[i]

# note 이름만 일렬로 출력
for student in students:
    print(student[0], end=' ')