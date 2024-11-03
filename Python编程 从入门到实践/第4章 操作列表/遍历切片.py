#切片(slice),提取列表中部分元素
players = ['charles','martina','michael','florence','eli']
print(players[1:3])
#[起始索引：终止索引]，也可以不指定索引默认为列表开头或列表结尾
#也可以通过负数索引返回与列表末尾相应距离的元素
print(players[:-2])
#设定步长，使python在指定范围内每隔几个元素提取一个
print(players[1:5:2])
print('-----------------------------分割线------------------------')
#用for循环使用切片，以遍历列表中部分元素
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
