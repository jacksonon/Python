# 继承和多态

class Animal(object):
    def run(self):
        print('动物在跑!')

class Dog(Animal):
    pass

class Cat(Animal):
    def run(self):
        print('猫在跑！')
    
    def eat(self):
        print('猫饿了，在吃饭！')


dog = Dog()
cat = Cat()

dog.run()
cat.run()
cat.eat()

a = list()
b = Animal()
c = Dog()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())



# 鸭子类型:动态语言，一个对象只要看起来像鸭子，走起路来像鸭子，那它就可以被看做是鸭子
class Timer(object):
    def run(self):
        print('时间滴滴答答的再走')

run_twice(Timer())

        


# isinstance(a, list)
# isinstance(b, Animal)
# isinstance(c, Dog)
# isinstance(c, Animal)

