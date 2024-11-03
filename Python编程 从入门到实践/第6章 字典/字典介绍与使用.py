#字典可存储的信息量不受限制
alien_0 = {'color':'green', 'points':5}
#键值对包含两个相互关联的值
#如要获取与键相关的值，指定字典名并把键放在后面的方括号里面
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
print("----------------------------分割线---------------------------")

#字典是一种动态结构，可随时在其中添加键值对
#可对字典alien_0添加两项信息：外星人的x坐标与y坐标
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#字典会保留定义时的元素排列顺序，元素排列顺序与其添加顺序相同
#定义空字典可以alien_0 = {}
print("----------------------------分割线---------------------------")

#修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0['color'])
#示例:
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")
#向右移动外星人，根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #这个外星人的移动速度肯定很快
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
print("----------------------------分割线---------------------------")

#删除键值对，使用del语句
alien_0 = {'color':'green', 'points':5}
print(alien_0)
del alien_0['points']
print(alien_0)
print("----------------------------分割线---------------------------")

#由类似的对象组成的字典
favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
    }
language = favorite_language['sarah'].title()
print(f"Sarah's favorite language is {language}.")
print("----------------------------分割线---------------------------")

#get()函数来访问值，若没有则返回指定的默认值
#第一个参数用于指定键，第二个参数为指定的键不存在时要返回的值
alien_0 = {'color':'green','speed':'slow'}
point_value = alien_0.get('points','No point value assigned.')
print(point_value) 