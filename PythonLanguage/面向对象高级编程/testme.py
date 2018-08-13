# TDD 测试驱动开发

class Dict(dict):
    '''
    自定义的文档测试.

    举例：
    
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    
    '''
    def __init__(self, **kw):
        super().__init__(**kw)
    # def __getattr__(self, key):
    #     try:
    #         return self[key]
    #     except KeyError:
    #         raise AttributeError(r"'Dict' object has no attribute '%s' " % key)
    def __setattr__(self, key, value):
        self[key] = value

import unittest
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1 , b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
    def setUp(self):
        print('初始化操作')
    def tearDown(self):
        print('结束操作')

if __name__ == '__main__':
    # 单元测试
    # unittest.main()

    # 文档测试
    import doctest
    doctest.testmod()