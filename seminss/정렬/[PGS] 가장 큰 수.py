#2:20~3:00 -> 풀이 확인

def solution(numbers):
    numbers=list(map(str,numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer=str(int(''.join(numbers)))
    return answer

# list와 map을 사용해 int형 list를 손쉽게 str형으로 변환 할 수 있다.
# 마지막에 str->int->str 한 건 '000','00'이 나올 경우 '0'으로 줄이기 위해서다.
# x*3을 사용하는 이유는 숫자의 범위가 0 이상 1,000 이하이기 때문이다.

# x가 2일 때: 222
# x가 21일 때: 212121
# x가 223일 때: 223223223
# x가 9일 때: 999
# x가 513일 때: 513513513
# x가 87일 때: 878787

# x를 세 번 반복해서 문자열로 만들기 때문에, 원래 숫자의 크기에 상관없이 비교할 수 있다. 
# 21은 2보다 크지만 x*3을 사용하면 212121로 변환되어서 2보다 큰 값으로 인식된다. 
# 마찬가지로 513은 51보다 크지만 x*3을 사용하면 513513513으로 변환되어 51보다 큰 값으로 인식된다.

# 만약 3이 아니라 다른 수를 이용한다면 숫자 비교가 제대로 이루어지지 않는다.
# x가 2이고 x*4를 사용한다면 2222가 된다.
# 이 경우 2222보다 22가 더 큰 수로 인식될 수 있다.

