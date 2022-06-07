# 1. import 패키지.모듈
from unit import character, item, monster
item.test()

from unit import *
character.test()
item.test()
monster.test()

import unit
unit.character.test()