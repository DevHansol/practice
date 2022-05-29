a = []
sum = 0

x = int(input('1일차 턱걸이 횟수>>>'))
a.append(x)
x = int(input('2일차 턱걸이 횟수>>>'))
a.append(x)
x = int(input('3일차 턱걸이 횟수>>>'))
a.append(x)
x = int(input('4일차 턱걸이 횟수>>>'))
a.append(x)
x = int(input('5일차 턱걸이 횟수>>>'))
a.append(x)
x = int(input('6일차 턱걸이 횟수>>>'))
a.append(x)
x = int(input('7일차 턱걸이 횟수>>>'))
a.append(x)

for i in range(7):
    sum += a[i]

average = sum/len(a)

print(a)
print(average)