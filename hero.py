class superhero:
    people = 'People'

    def __init__(self,name,nickname,superpower,health_points,catchphrase):
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
        return f'Nickname - {self.nickname}\n'\
               f' Superpower -  {self.superpower}\n'\
               f' Catchphrase - "{self.catchphrase}"'
    
    def __len__(self):
        return len(self.catchphrase)

Hero = superhero('Nazira','Angelus','sorceress', 100, 'Never give up')

print(f' {Hero.people}\n {Hero.h_name()}\n {Hero.hp()}\n {Hero}\n Number of letters in catchphrase -> {len(Hero)}')


