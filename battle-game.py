import random_calc as ra
from character_class import Character
from photo_app import Application



#敵キャラクターのエンカウント抽選

enemy_name, enemy_hp , photo_number= ra.random_encounter()


#自分の情報の入力
 
my_name = ra.character_name_select()

print('==============================================')


#自分と敵のobjectを生成

my_chara = Character(my_name, 200)
enemy = Character(enemy_name, enemy_hp)

print(f'{enemy.name}が現れた')

app = Application()
app.main_page.create_widgets(photo_data=photo_number, my_name=my_chara.name, enemy_name=enemy.name)
app.mainloop()

app.after(10000,app.destroy)



#バトルのコード

while my_chara.hp > 0 and enemy.hp > 0:
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('')
    print(f'{my_chara.name}のHPは{my_chara.hp}.MPは{my_chara.mp}です')
    print('')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('-------------------------------------------------')
    my_attack = 0
    input_my_attack = input(
        '攻撃内容: 1.攻撃スキル、2.回復魔法（消費ｍｐ５）、3.攻撃魔法（消費ｍｐ１０）::数字で入力してください::')
    my_attack = int(input_my_attack) if input_my_attack.isdigit() else my_attack

    '''
    自分の攻撃

    '''

    if my_attack == 1:
        
        attack_name, skill_damage = Character.my_attack_action(1)

        enemy.hp -= skill_damage

        print(f'{my_chara.name}は{attack_name} を発動した!!')
        print(f'{enemy.name}に{skill_damage}を与えた!!')

    elif my_attack == 2:
        
        if my_chara.mp >= 5:
            attack_name, recover = Character.my_attack_action(2)
            my_chara.hp += recover
            my_chara.hp = 200 if my_chara.hp >= 200 else my_chara.hp
            my_chara.mp -= 5
            print(f'{my_chara.name}は回復魔法をつかった!')
            print(f'{my_chara.name}のHPは{recover}回復した!!')
        else:
            print(f'あなたは回復魔法をつかった!')
            print('MPが足りません!! 回復できませんでした')

    elif my_attack == 3:
        
        if my_chara.mp >= 10:
            attack_name, magic_damage = Character.my_attack_action(3)
            my_chara.mp -= 10
            enemy.hp -= magic_damage
            print(f'{my_chara.name}は{attack_name} を発動した!!')
            print(f'{enemy.name}に{magic_damage}を与えた!!')
        else:
            print('MPが足りません!! 攻撃できませんでした')

    else:
        attack_name, attack_damage = Character.my_attack_action(0)
        enemy.hp -= attack_damage

        print(f'{my_chara.name}は{enemy.name}に{attack_damage}ダメージを与えた!')

    print('===================================================')

    '''
    敵の攻撃

    '''
    if enemy.hp <= 0:
        break
    attack_name, damage = enemy.monster_action_select()

    my_chara.hp -= damage
    print('')
    print(f'{enemy.name}は{my_chara.name}に{attack_name}で{damage}ダメージを与えた!')

'''
バトル終了のプログラム

'''
result = f'{my_chara.name}は{enemy.name}をたおした'if enemy.hp <= 0 else f'あなたは負けました'
print(result)
print('')
print('お疲れ様でした。また遊んでください!!')
print('')
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
