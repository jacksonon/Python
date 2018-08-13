# 多重继承

class Student(object):
    def __init__(self):
        self.name = name

    # 重写描述
    def __str__(self):
        return 'Student object (name: %s)' %s self.name        

    # 偷懒写法
    __repr__ = __str__


print(Student('瓦美好口岸为'))

# 定制类

class Chain(object):
    def __init__(self, path=''):
        self._path = path
        self.a, self.b = 0, 1
    
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

    def __str__(self):
        return self._path

    def __call__(self):
        print('my name is %s' % self._path)

    __repr__ = __str__


for n in Chain():
    print (n)

print(Chain().status.user.timeline.list)

s = Chain('路径是额很么')
print(s())

# 怎么判断一个变量是对象还是函数呢
callable(Chain('jeje'))
callable(max)
callable([1, 2 , 3])
