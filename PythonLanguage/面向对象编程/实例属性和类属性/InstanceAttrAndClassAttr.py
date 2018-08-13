# 实例属性和类属性

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90


>>> class StudentCount(object):
...     count = 0
...     def __init__(self, name):
...             self.name = name
...             self.count = self.count + 1
... 
>>> sc = StudentCount('王家伟')
>>> sc.name
'王家伟'
>>> sc.count
1
>>> sc1 = StudentCount('刘亦菲')
>>> sc1.name
'刘亦菲'
>>> sc1.count
1
>>> StudentCount.count += 1
>>> StudentCount.count
1
>>> StudentCount.count += 1
>>> StudentCount.count
2
>>> 