
class SuperHero:
    people = 'People'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def h_name(self):
        return f'The name of hero is {self.name}'

    def hp(self):
        return f'Condition of health - {self.health_points * 2}'

    def __str__(self):
        return f'Nickname - {self.nickname}\n' \
               f' Superpower -  {self.superpower}\n' \
               f' Catchphrase - "{self.catchphrase}"'

    def __len__(self):
        return len(self.catchphrase)


class HeroWar(SuperHero):
    hero = 'Hero of World War 2'
    

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage = False, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase

    def hp(self):
        self.fly = True
        return f'Condition of health - {self.health_points ** 2}\n {self.fly} '

    def __str__(self):
        return f'fly in the {self.fly}_phase\n'\
               f' Nickname - {self.nickname}\n' \
               f' Superpower -  {self.superpower}\n'\
               f' Catchphrase - "{self.catchphrase}"'\

class HeroSpace(SuperHero):
    hero = 'Hero of Space'
   
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage = False, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase

    def hp(self):
        self.fly = True
        return f'Condition of health - {self.health_points ** 2}\n {self.fly} '

    def __str__(self):
        return f'fly in the {self.fly}_phase\n'\
               f' Nickname - {self.nickname}\n' \
               f' Superpower -  {self.superpower}\n'\
               f' Catchphrase - "{self.catchphrase}"'\

class Villain(HeroSpace):
    people = 'Monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase

    def __str__(self):
        return f'fly in the {self.fly}_phase\n'\
               f' Nickname - {self.nickname}\n' \
               f' Superpower -  {self.superpower}\n' \
               f' Catchphrase - "{self.catchphrase}"' \

    def gen_x(self):
        pass

    def crit(self):
        self.damage = self.damage ** 2
        return self.damage

Hero = SuperHero('Nazira', 'Angelus', 'sorceress', 100, 'Never give up!')
Hero1 = HeroWar('Suimonkul', 'Shopokov', 'super-soldier', 100, 'Всегда готов!')
Hero2 = HeroSpace('Yuriy', 'Gagarin', 'first_spaceman', 100, 'Если быть, то быть первым!')
Monster = Villain('Tom Riddle', 'Lord Voldemort', 'Dark wizard', 200, 'There is no good and evil')

print(f'{Hero.people}\n {Hero.h_name()}\n {Hero.hp()}\n {Hero}\n'
      f'Number of letters in catchphrase -> {len(Hero)}\n')

print(f'{Hero1.hero}\n {Hero1.h_name()}\n {Hero1.hp()}\n {Hero1}\n'
      f'Number of letters in catchphrase -> {len(Hero1)}\n')

print(f'{Hero2.hero}\n {Hero2.h_name()}\n {Hero2.hp()}\n {Hero2}\n'
      f'Number of letters in catchphrase -> {len(Hero2)}\n')

print(f'{Monster.people}\n {Monster.h_name()}\n {Monster.hp()}\n {Monster}\n'
      f'Number of letters in catchphrase -> {len(Monster)}\n')

print(' Степень урона --> ', Monster.crit())
