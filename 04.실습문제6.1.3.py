import random

def getRandomNumber():
    x = random.randint(1, 45)
    return x

if __name__ == '__main__':
    count = 0
    num = []
    x = 0

    while True:
        if count > 5:
            break
        x = getRandomNumber()
        if x not in num:
            num.append(x)
            count += 1

    print(num)