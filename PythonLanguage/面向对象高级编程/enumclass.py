# 使用枚举类

from enum import Enum

Month = Enum('Month', ('一月', '二月', '三月'))

for name, member in Month.__members__.items():
    print(name, member, member.value)
