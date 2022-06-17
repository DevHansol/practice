import csv

data = [
    ['이름', '반', '번호'],
    ['재석', 1, 20],
    ['홍철', 3, 8],
    ['형돈', 5, 32]
]

file = open('student.csv', 'w', newline = '', encoding = 'utf-8-sig') # newline은 csv를 만들 때 자동으로 한줄을 건너 뛰는것을 방지함
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()