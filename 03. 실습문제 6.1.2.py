def printSumAvg(x, y, z):
    sum = x + y + z
    avg = sum/3
    print('합계:', sum, ' 평균:', avg)
    print(f'합계: {sum}, 평균: {avg}')

if __name__ == '__main__':
    printSumAvg(10, 20, 30)