#嵌套：可以将多个字典存储在列表中，或将列表作为值存储在字典中
alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red' ,'point': 15}

aliens =[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
print("----------------------------分割线---------------------------")

#创建一个用于存储外星人的空列表
aliens = []
#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green','points': 5,'speed': 'slow'}
    aliens.append(new_alien)
#修改前3个外星人为黄色、速度中值且值为十分
for alien in aliens[:4]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
#可进一步扩展这个循环，将黄色外星人改成红色外星人
for alien in aliens[:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
#显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}")
print("----------------------------分割线---------------------------")

#在字典中存储列表
#存储顾客所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings':['mushroom','extra cheese'],
    }
#概述顾客点的披萨
print(f"You ordered a {pizza['crust']}-crust pizza"
    "with the following toppings")
for topping in pizza ['toppings']:
    print(f"\t{topping}")
print("----------------------------分割线---------------------------")

#将一个键关联到多个值
favorite_languages = {
    'jen': ['python','rust'],
    'sarah': ['c'],
    'edward': ['rust','go'],
    'phil': ['python' ,'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:      
        print(f"\n{name.title()}'s favorite languages are")
    else:
        print(f"\n{name.title()}'s favorite languages is")
    for language in languages:
        print(f"\t{language.title()}")
print("----------------------------分割线---------------------------")

#字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }
for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print (f"\tFull name: {full_name.title()}")
    print (f"\tLocation: {location.title()}")


    
