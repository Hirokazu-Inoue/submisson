import random

#敵をランダムに生成
def random_encounter():
    enemy = {'スライム':[100, 3], 'ドラゴン': [1000, 1 ], '魔王': [1500, 2], '大魔王': [2000, 0]}

    random_key = random.randint(0, len(enemy) - 1)
    name_key = list(enemy.keys())

    enemy_name = name_key[random_key]
    enemy_hp = enemy[enemy_name][0]
    photo_data = enemy[enemy_name][1]

    return enemy_name, enemy_hp, photo_data
def character_name_select():
    my_names = ['くっきー','しばづけ','たくわん','はくさい','ちょこ','ちぇりー','ばなな','りんご',]
    my_name_number = random.randint(0, len(my_names) - 1)
    my_name = my_names[my_name_number]
    return my_name

#ダメージ計算
def calc_damage(attacks, weights):
    attack = list(attacks.keys())
    attack_key = random.choices(attack, weights=weights, k=1)[0]
    par1, par2 = attacks[attack_key]
    damage = random.randint(par1, par2)
    return attack_key, damage  
