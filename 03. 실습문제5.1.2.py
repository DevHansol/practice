time_count = int(input("공부 시간을 입력하세요(시간) >>>"))

if time_count >= 10:
    print('휴대폰 잠금이 해제됩니다.')

elif time_count >=5:
    print('휴대폰을 30분간 사용가능합니다.')

else:
    print('휴대폰 사용이 불가능합니다')