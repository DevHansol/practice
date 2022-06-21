if __name__ == "__main__":
    tmp = 0
    while(True):
        print("\n\n- FASTCAMPUS BLOG -")
        print("- 메뉴를 선택해 주세요 -")
        print("1. 게시글 쓰기")
        print("2. 게시글 목록")
        print("3. 프로그램 종료")
        try:
            tmp = int(input(">>>"))
        except ValueError:
            print("숫자를 입력해 주세요")
        else:
            if tmp == 1:
                print("게시글 쓰기")
                post = Post(input(""))

            elif tmp == 2:
                print("게시글 목록")

            elif tmp == 3:
                print("프로그램 종료!!")
                break

            else:
                print("잘못 입력했습니다!!")
