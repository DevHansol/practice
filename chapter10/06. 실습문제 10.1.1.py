# 오류 해결 과정 중심!!


import csv

# data = [
#     ['종목', '매입가', '수량', '목표가'],
#     ['삼성전자', 85000, 10, 90000],
#     ['NAVER', 380000, 5, 400000],
# ]
#
# file = open('mystock.csv', 'w', newline = '', encoding = 'utf-8-sig')
# writer = csv.writer(file)
#
# for d in data:
#     writer.writerow(d)
# file.close()

def show_profit(data):
    name = data[0] # 종목
    purchase_price = int(data[1]) # 매입가
    amount = int(data[2])
    goal = int(data[3])

    profit = (goal - purchase_price) * amount
    profit_ratio = (goal / purchase_price - 1) * 100

    print(f'{name} {profit:.2f} {profit_ratio:.2f}')
if __name__ == '__main__':
    file = open('mystock.csv', 'r', encoding = 'UTF-8') # 파일 열기
    reader = list(csv.reader(file)) # 파일 데이터 읽기
    for data in reader[1:]:
        show_profit(data)
    file.close()