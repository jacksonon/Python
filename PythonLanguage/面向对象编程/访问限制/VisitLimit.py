class Stu(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s : %s' % (self.__name, self.__score))

    def getName(self):
        return self.__name

    def getScore(self):
        return self.__score
    
    def setName(self, name):
        self.__name = name
    
    def setScore(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('分数值不可以小于0或大于100')
        
me = Stu('王家伟', 100)
me.print_score()
me.setName('我的新名字')
me.setScore(88)
me.print_score()

print('%s' % me.getName())
print('%d' % me.getScore())

    
        
        
        
        