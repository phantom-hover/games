from pathlib import Path

def count_words(path):
    """计算一个文件大致包含多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    # 让程序静默失败
        print(f"Sorry, the file {path} does not exist.")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['D:\\Desktop\\alice.txt',
             'D:\Desktop\python_work\Python编程 从入门到实践\text_files\siddhartha.txt',
             'D:\Desktop\python_work\Python编程 从入门到实践\text_files\mody_dick.txt',
             'D:\Desktop\python_work\Python编程 从入门到实践\text_files\little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
    #即使文件不存在，仍然不影响这个程序处理其他文件