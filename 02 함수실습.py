# 기본형
# 1. 정의하기
import random

def printHello():
    print('Hello')

# 매개변수가 있는 함수
def sum(a, b):
    print(a+b)

# 반환값이 있는 함수
def getRandomNumber():
    number = random.randint(1, 10)
    return number

# 매개변수와 반환값이 있는 함수
def add(a, b):
    result = a + b
    return result

#2. 호출하기
if __name__ == '__main__':
    printHello()
    sum(5, 10)
    print(getRandomNumber())
    print(add(10, 10))
