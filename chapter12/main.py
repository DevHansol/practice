import os
import csv
from post import Post

file_path = "./data.csv"

# 게시글 쓰기
def write_post():
    print("\n\n - 게시글 쓰기 -")
    title = input("제목을 입력해 주세요\n>>>")
    content = input("내용을 입력해 주세요\n>>>")

    # 글번호
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("# 게시글이 등록되었습니다.")

def list_post():
    """
    게스글 목록
    """
    id_list = []
    for post in post_list:
        print("\n\n - 게시글 목록 -")
        print(f"번호: {post.get_id()}")
        print(f"제목:  {post.get_title()}")
        print(f"조회수: {post.get_view_count()}")
        id_list.append(post.get_id())

    while True:
        try:
            id = int(input("\nQ) 글 번호를 선택해 주세요 (메뉴로 돌아가려면 -1을 입력)\n>>>"))
            if id in id_list:
                print("- 게시글 상세보기- ")
                print("번호:", post.get_id())
                print("제목:", post.get_title())
                print("본문:", post.get_content())
                print("조회수:", post.get_view_count())

                try:
                    num = int(input("Q) 수정: 1 삭제: 2 (메뉴로 돌아가려면 -1을 입력"))

                    if num == 1:
                        string = input(">>>")
                        post.set_post(id, post.get_title(), string, post.get_view_count())
                    elif num == 2:
                        del id_list[id]
                    elif num == -1:
                        break

                except ValueError as e:
                    print("숫자를 입력해 주세요")
            elif id == -1:
                break
            else:
                print("없는 글 번호 입니다.")
        except ValueError:
            print("숫자를 입력해 주세요")


if __name__ == '__main__':
    # post 객체를 저장할 리스트
    post_list = []

    # data.csv 파일이 있다면
    if os.path.exists(file_path):
        print("게시글 로딩중...")

        f = open(file_path, "r", encoding="utf8")
        reader = csv.reader(f)
        for data in reader:
            # Post 인스턴스 생성하기
            post = Post(int(data[0]), data[1], data[2], int(data[3]))
            post_list.append(post)
    else:
        # 파일 생성하기
        f = open(file_path, 'w', encoding="utf8", newline="")
        f.close()

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
                write_post()

            elif tmp == 2:
                list_post()

            elif tmp == 3:
                print("프로그램 종료!!")
                break

            else:
                print("잘못 입력했습니다!!")
