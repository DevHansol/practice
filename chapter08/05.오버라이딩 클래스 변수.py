# 상속
# 클래스들에 중복된 코드를 제거하고 유지보수를
# 편하게 하기 위해서 사용.

# 클래스 변수
# : 인스턴스들이 모두 공유하는 변수
import random

# 부모 클래스
class Monster:
    max_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self): # 메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack) # 몬스터의 init을 상속받는다
        self.skills = ('브레스', '꼬리치기', '날개치기')

    def move(self):
        print(f'[{self.name}] 날기')

    def skill(self):
        print(f'[{self.name}] 스킬 사용 {self.skills[random.randint(0, 2)]}')

wolf = Wolf("울프", 1500, 200)
wolf.move()

shark = Shark('상어', 3000, 400)
shark.move()

dragon = Dragon('드래곤', 8000, 800)
dragon.move()
dragon.skill()
print(wolf.max_num)