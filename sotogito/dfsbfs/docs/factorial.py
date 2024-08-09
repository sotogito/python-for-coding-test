"""
재귀함수를 사용한 팩토리얼 구현

factorial_recursive(5)를 호출합니다.
n이 1보다 크므로 5 * factorial_recursive(4)를 계산합니다.
factorial_recursive(4)를 호출합니다.
이때, n = 4이므로 4 * factorial_recursive(3)을 계산합니다.
factorial_recursive(3)를 호출합니다.
n = 3이므로 3 * factorial_recursive(2)를 계산합니다.
factorial_recursive(2)를 호출합니다.
n = 2이므로 2 * factorial_recursive(1)을 계산합니다.
factorial_recursive(1)를 호출합니다.
n = 1이므로 1 * factorial_recursive(0)을 계산합니다.
factorial_recursive(0)를 호출합니다.
n = 0이므로 기저 조건에 의해 1을 반환합니다.



"""
def factorial_recursive(n): #note 재귀함수 구현
    if n < 1: #note 기저조건 :  이 조건이 충족되면 함수는 더 이상 재귀적으로 자신을 호출하지 않고, 단순히 1을 반환. 즉 1 이하면 1반환하고 끝남.
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n): #note 반복문 구현
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

print(factorial_recursive(5))



print(factorial_iterative(5))