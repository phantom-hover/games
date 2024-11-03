first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
#在左引号前面加入f，这种字符串称为f字符串（format）
message = f"Hello, {full_name.title()}"
print (message)
#还可以使用f字符串来创建消息，再把整条消息赋予变量

print("language:\n\tPython\n\tC\n\tJavaScript")
#添加制表符，使用字符组合\t
#添加换行符，使用字符组合\n

favorite_language = '  Python  '
a = favorite_language.strip()
b = favorite_language.lstrip()
c = favorite_language.rstrip()
print(a,b,c)
#可以删除空白、左空白、右空白，可分别使用strip(),lstrip(),rstrip()方法

nostarch_url = 'http://nostarch.com'
simple_url = nostarch_url.removeprefix('http://')
print(simple_url)
#removeprefix()保持原始字符串不变，而在括号内输入要从原始字符串中删除的前缀