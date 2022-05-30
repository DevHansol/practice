korean = ['사랑해', '귀엽다', '고마워', '행복해']
score = 0

print("Let's Learning Korean")

for word in korean:
    print(word)
    language = input()

    if word == language:
        score += 1
    else:
        pass
    # 전체 문제 개수: 4개
    # 맞힌 문제 개수: 2개
    # 틀린 문제 개수: 2개
print('전체 문제 개수:', len(korean), '개')
print('맞힌 문제 개수:', score, '개')
print('틀린 문제 개수:', len(korean) - score, '개')