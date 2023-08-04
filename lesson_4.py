from enum import Enum
from random import choice, randint

class SuperAbulity(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEALTH = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    NONE = 5

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage
        
    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value
    
    @property
    def damage(self):
        return self.__damage
    
    @damage.setter
    def damage(self, value):
        self.__damage = value
    
    def __str__(self):
        return f'{self.__name}, health: {self.__health}, damage: {self.__damage}'
    


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = SuperAbulity.NONE
        self.__stun_duration = 0

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        if self.__stun_duration == 0: 
            hero = choice(heroes)
            self.__defence = hero.ability
        else:
            print(f"{self.name} is stunned and skips this round!")
            self.decrease_stun_duration()

    def attack(self, heroes):
        if self.__stun_duration == 0: 
            for hero in heroes:
                if hero.health > 0:
                    if hero.ability == SuperAbulity.BLOCK_DAMAGE_AND_REVERT:
                        hero.blocked_damage = int(self.damage / 5)
                        hero.health -= int(self.damage - hero.blocked_damage)
                    else:
                        hero.health -= self.damage

    def decrease_stun_duration(self):
        if self.__stun_duration > 0:
            self.__stun_duration -= 1

    def reset_stun_duration(self):
        self.__stun_duration = 0

    def handle_turn(self, heroes):
        self.choose_defence(heroes)
        self.attack(heroes)

    def __str__(self):
        return 'BOSS: ' + super().__str__() + f', defense: {self.__defence.name}, stun duration: {self.__stun_duration}'
    
     
class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if isinstance(ability, SuperAbulity):
            self.__ability = ability
        else:
            ValueError('Wrong data type for ability')
        
    @property
    def ability(self):
        return self.__ability
    
    def attack(self, boss): 
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage
    
    def apply_super_power(self, boss, heroes):
        pass
    
    def __str__(self):
        return super().__str__() + f' ability: {self.__ability}'
    

class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbulity.CRITICAL_DAMAGE)
        
    def apply_super_power(self, boss, heroes):
        hitCritically = self.damage * randint(2, 7)
        boss.health -= hitCritically
        print(f'Warrior: {self.name}, hit critically: {hitCritically}')
    
    
class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbulity.BOOST)
        self.__boost_amount = 0
        self.__is_alive = True
        
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.__is_alive = False
            self.__boost_amount = 0
    
    def apply_super_power(self, boss, heroes):
        if self.__is_alive:
            self.__boost_amount = 5
            for hero in heroes:
                if hero.health > 0:
                    hero.damage += self.__boost_amount
    
    def __str__(self):
        return super().__str__() + f', ability: {self.ability}, boost amount: {self.__boost_amount}, alive: {self.__is_alive}'

    
class Berserc(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbulity.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0
        
    @property
    def blocked_damage(self):
        return self.__blocked_damage
    
    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value
        
        
    def apply_super_power(self, boss, heroes):
        boss.health -= self.blocked_damage
        print(f'Berserk: {self.name}, reverted: {self.blocked_damage}')    
    

class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbulity.HEALTH)
        self.__heal_points = heal_points
        
    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points
            
                
class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbulity.NONE)
        self.__stun_duration = 0

    def apply_super_power(self, boss, heroes):
        if self.health > 0 and boss.health > 0:
            stun_chance = randint(1, 100)
            if stun_chance <= 30: 
                self.__stun_duration = 1
                self.attack(boss)

    def attack(self, boss):
        if self.__stun_duration > 0:
            print(f'{boss.name} is stunned and misses this round!')
        else:
            super().attack(boss)
    
    def __str__(self):
        return super().__str__() + f', ability: {self.ability}'

    
round_number = 0
        
def show_stats(boss, heroes):
    print(f'Round: {round_number} ---------')
    print(boss)
    for hero in heroes:
        print(hero)
        
def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!')
    return all_heroes_dead
        
def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if boss.defence != hero.ability:
            hero.attack(boss)
            if hero.health > 0 and boss.health > 0:
                hero.apply_super_power(boss, heroes)
    show_stats(boss, heroes)        
        
def start_game():
    boss = Boss('Doom', 1000, 50)
    
    warrior = Warrior('Superman', 270, 10)
    doc = Medic('Aibolit', 250, 5, 15)
    magic = Magic('Hendolf', 260, 15)
    berserc = Berserc('Garol', 270, 10)
    assistant = Medic('Haus', 260, 5, 5)
    thor = Thor('Thor', 300, 20)
    
    heroes_list = [warrior, doc, magic, berserc, assistant, thor]
    
    show_stats(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)

start_game()