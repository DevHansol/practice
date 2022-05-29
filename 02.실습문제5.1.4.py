korean = int(input('국어 >>>'))
math = int(input('수학>>>'))
english = int(input('영어>>>'))

average = (korean+math+english)/3

if korean <0 or math < 0 or english < 0 or korean > 100 or math > 100 or english > 100:
    print('잘못 입력하였습니다')

elif average > 80:
    print('합격')

else:
    print('불합격')