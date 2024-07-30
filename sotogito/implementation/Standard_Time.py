"""
if i == standard_number or j == standard_number or k == standard_number:
위에같이 3을 확인하면 만약 13, 35,33의경우는 해당이 됮 않고 온전히 숫자 3일경우만 count되어지기 떄문에 틀리다.

그래서 숫자에 해당 숫자가 들어갔는지 확인하기 위해서는 int 타입이 아니라 string타입으로 검사해야한다.

"""




n = int(input())

hour = n
minute = 59
second = 59

standard_number_str = '3'

count = 0

for i in range(n, -1, -1): # range(hour+1)
    for j in range(minute, -1, -1): #range(60)
        for k in range(second, -1, -1): #range(60)
            if standard_number_str in str(i) + str(j) + str(k):
                count += 1

print(count)