# 获取对象信息

type(123)
type('str')
type(None)

# 判断一个对象是否是函数
import types

def fn():
    pass

type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType


# 总是优先使用isinstance()判断类型，可以将制定类型及其自雷一网打尽
isinstance('a', str)


# 获取一个对象的所有属性和方法
dir('ABC')

