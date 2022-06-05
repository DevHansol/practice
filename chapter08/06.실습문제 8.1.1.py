import random

class item():
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    def output(self):
        print(self.name)
        print(self.price)
        print(self.weight)
        print(self.isdropable)

    def sale(self):
        print(f'[{self.name}] 판매가격은 [{self.price}]')

    def discard(self):
        if self.isdropable:
            print(f"{self.name}은 버렸습니다.")
        else:
            print(f'{self.name}은 버릴 수 없습니다.')

class WearableItem(item):
    def __init__(self, name, price, weight, isdropable):
        super().__init__(name, price, weight, isdropable)
        self.effect = ('공속 증가', '마나 증가', '버프 향상')

    def Wear(self):
        print(f'{self.name}을 착용했습니다.')
        print(f'{self.effect[random.randint(0, 2)]}가 적용되었습니다.')


class UsableItem(item):
    def __init__(self, name, price, weight, isdropable):
        super().__init__(name, price, weight, isdropable)
        self.effect = ('체력 회복', '마나 회복')

    def Use(self):
        print(f'{self.name}을 사용합니다.')
        print(f'{self.effect[random.randint(0, 1)]}합니다')


if __name__ == '__main__':
    sword = WearableItem('강철검', 10000, 80, True)
    sword.Wear()
    sword.sale()
    sword.discard()

    potion = UsableItem('마녀의 피', 500, 10, False)
    potion.Use()
    potion.sale()
    potion.discard()