# 序列化

import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
    

s = Student('王家伟', 200, 100)
new = json.dumps(s, default=lambda obj: obj.__dict__)

json_str = '{"name": "Bob", "age": 20, "score": 88}'
print(json.dumps(json_str, object_hook=dict2student))

        