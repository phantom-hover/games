#遍历所有键值对
#item()函数，返回一个键值对列表
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key , value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")
print("----------------------------分割线---------------------------")

#keys()函数，遍历字典中所有的键
for value in user_0.keys():
    print(value.title())
#key()方法可以让代码更易理解，也可以省略
#if语句中key()方法还能返回一个列表，包含字典中的所有键
if 'erin' not in user_0.keys():
    print("Erin, please take our poll!")

#按特定顺序遍历字典所有的键，可以用sorted()函数
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name in sorted(favorite_language.keys()):
    print(f"{name.title()},thank you for taking the poll.")
#对于方法dictionary.keys()的结果调用了sorted()函数，让其在遍历前对这个列表进行排序
print("----------------------------分割线---------------------------")

#遍历字典中的所有值，可以使用values()方法，返回一个值的列表
#用set()可以剔除重复项,再利用sorted()进行排序
print("The following languages have been mentioned:")
for language in sorted(set(favorite_language.values())):
    print(language.title())


