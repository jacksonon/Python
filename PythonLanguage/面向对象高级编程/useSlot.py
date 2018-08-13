# 使用__slot__

# 定义一个class 创建实例后 可以给实例绑定任何属性和方法，动态语言灵活性

class Student(object):
    pass

s = Student()
s.name = '王家伟'
print(s.name)


# 给实例绑定方法，只对当前实例起作用
def set_age(self, age):
    self.age = age

from types import MethodType
# 给实例绑定方法，使用types模块内部的MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 给类绑定方法，对类的所有实例都起作用
def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
print(s.score)

# 限制添加的实例属性
class NewSstudent(object):
    __slot__ = ('name', 'score')

class Std2(NewSstudent):
    pass

class Std3(NewSstudent):
    # 持有的slot实例
    __slot__ = ('age')

