from random_calc import calc_damage

'''キャラクター関連の主にアクションデータが入ったクラスです

'''
class Character:
    
    def __init__(self,name,hp,mp = 100):
        self.name = name
        self.hp = hp
        self.mp = mp



    def monster_action_select(self):
        if self.name == 'スライム':
            attacks = {'痛恨の一撃':[100, 150], '通常攻撃':[20, 30]}
            w = [3,1] 
               
        if self.name == 'ドラゴン':
            attacks = {'痛恨の一撃':[70, 80], 'ブレス': [50, 60], '通常攻撃': [40, 50]}
            w = [0.3,1,1]
            
        if self.name == '魔王':
            attacks = {'痛恨の一撃':[70, 80], '魔法攻撃': [50, 60], '通常攻撃': [40, 50]}
            w = [0.7,1,1]
            
        if self.name == '大魔王':
            attacks = {'痛恨の一撃':[70, 80], '魔法攻撃': [50, 60], '通常攻撃': [40, 50]}
            w = [1,1,1] 

        attack_name, damage = calc_damage(attacks, w)     
        return attack_name, damage
        
    @staticmethod
    def my_attack_action(attack_number):
        if attack_number ==1 :
            attacks = {'攻撃スキル': [50, 60], '攻撃スキルのクリティカルヒット': [100, 120]}
            w = [4, 1]

        if attack_number == 2:
            attacks = {'回復魔法':[100, 150]}
            w = [1]

        if attack_number == 3:
            attacks = {'攻撃魔法': [70, 80], '攻撃魔法のクリティカルヒット': [120, 150]}
            w = [3, 1]

        if attack_number == 0:
            attacks = {'通常攻撃': [10, 20]}
            w = [1]

        attack_name, damage = calc_damage(attacks, w)
        return attack_name, damage
