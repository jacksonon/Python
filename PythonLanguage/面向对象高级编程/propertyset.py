# 使用@property

class MeSize(object):
    
    # get方法
    @property
    def resolution(self):
        return self._resolution
    
    # set方法
    @resolution.setter
    def resolution(self, value):
        self._resolution = value

    @property
    def age(self):
        return 2018 - self._resolution

a = MeSize()
a.resolution = 100
print(a.resolution)
print(a.age)