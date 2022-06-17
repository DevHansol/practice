import pickle

if __name__ == '__main__':
    # # 1. 파이썬 객체를 Pickle로 저장하기
    # data = {
    #     '목표1' : '매일 팔굽혀 펴기 100회',
    #     '목표2' : '매일 코딩 공부 1시간'
    # }
    #
    # file = open('data.pickle', 'wb')
    # pickle.dump(data, file)
    # file.close()

    file = open('data.pickle', 'rb')
    data = pickle.load(file)
    print(data)
    file.close()