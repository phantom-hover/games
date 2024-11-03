#JSON(JavaScript Object Notation)
#用json.dumps()存储,json.load()读取
from pathlib import Path
import json
#导入模块json，并创建一个数值列表
numbers = [2, 3, 5, 7, 11, 13]
#选择一个文件名，指定要将该数值存储到哪个文件中
path = Path('numbers.json')
contents = (json.dumps(numbers))
path.write_text(contents)

#使用json.loads()将这个列表读取到内存中
path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)

#保存和读取用户生成的数据
from pathlib import Path
import json

def greet_user():
    """问候用户，并指出其名字"""
    path = Path('username.json')
    if path.exists():
    #exist()方法：若指定的文件夹或文件存在，则返回True，否则返回False
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()