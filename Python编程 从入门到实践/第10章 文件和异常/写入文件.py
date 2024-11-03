#写入一行，定义一个文件的路径后，就可使用write_text()将数据写入该文件了
from pathlib import Path
path = Path("D:\\Desktop\\python_work\\Python编程 从入门到实践\\text_files\\programming.txt")
path.write_text("I love  programming")
#write_text()接受单个实参，即要写入文件的字符串
#注意：Python只能将字符串写入文件中。如果要将数值数据存储到文本文件中，必须先使用函数str()将其转化为字符串格式

#如果path变量对应的路径指向的文件不存在，就创建它
#写入多行：先创建一个字符串，再调用函数将这个字符串传递给它
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path.write_text(contents)

#谨慎调用write_text()函数，若指定的文件已存在，write_text()将删除其内容，并将指定的内容写入其中。