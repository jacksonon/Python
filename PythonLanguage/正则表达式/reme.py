# 正则表达式

# \d 一个数字
# \w 一个字母或数字
# . 匹配任意字符
# \s 匹配空格

# * 标识任意数量字符
# + 标识至少一个字符 >=1
# ？ 标识0或者1个字符  0 || 1
# {n} 标识n个字符
# {n,m} 标识n-m个字符

# \特殊字符 只标识这个特殊字符
# [] 表示范围
# a|b 可以匹配可以是2者中的1个
# ^ 表示开头
# $ 表示结尾

import re
test = '我的名字'
if re.match(r'^\w{0, 10}$', test):
    print('ok')
else:
    print('faile')


# 切分字符串：
'a b  c'.split(' ')
re.split(r'[\s\,\;]+', 'a b  cd    e')

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

# 编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()