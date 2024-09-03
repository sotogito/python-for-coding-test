"""
무슨 정렬 알고리즘을 사용할지는 입력 조건을 보고 결정하면 된다.
입력 정보는 다음과 같다.

1. 첫번째 줄에 학생 수 N이 입력된다 (1~1000,000)
2. 학생이름 성정 -> 의 양식으로 입력받아지며 학생 성적은 100이하의 자연수이다.

처음에는 선택정렬 풀었지만, 입력값이 만아질 경우를 고려하여 다른 정렬 알고리즘을 사용해야한다.

- 선택 정렬 : 입력값이 많아질 경우 불리하다.
- 삽입 정렬 : 데이터가 거의 정렬되어있는 상태인지 확인이 불가하다.
- 퀵 정렬 : 구현이 복잡하다
- 계수 정렬 : 빠르고 간단하며 정수일때 유리하다

떄문에 이 문제는 계수정렬로 푸는것이 유리하다.
하지만 나는 라이브러리를 이용하겠다.

"""
n = int(input())
students = []

for i in range(n):
    student = input().split()
    students.append(student)

result = sorted(students, key=lambda student: int(student[1]))

# note 이름만 일렬로 출력
for student in result:
    print(student[0], end=' ')


# note 선택정렬
"""
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if students[min_index][1] > students[j][1]:
            min_index = j

    students[i], students[min_index] = students[min_index], students[i]
"""
