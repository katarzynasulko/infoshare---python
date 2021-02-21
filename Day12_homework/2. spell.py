class Spell:
    def __init__(self, name):
        self.name = name
        self.result = 'Spelled'

    def cast_spell(self):
        print(f'{self.name} was casted. You are {self.result}!')
        print('')


class Charm(Spell):
    def __init__(self, name):
        super().__init__(name)
        self.result = 'charmed'

class Curse(Spell):
    def __init__(self, name):
        super().__init__(name)
        self.result = 'cursed'

class Jinx(Spell):
    def __init__(self, name):
        super().__init__(name)
        self.result = 'jinxed'

class Healing_spell(Spell):
    def __init__(self, name):
        super().__init__(name)
        self.result = 'healed'

class Modifier(Spell):
    def __init__(self, name):
        super().__init__(name)
        self.result = 'modified'

if __name__ == '__main__':

    avenseguim = Charm('Avenseguim')
    avenseguim.cast_spell()
    avada_kedavra = Curse('Avada Kedavra')
    avada_kedavra.cast_spell()
    anapneo = Healing_spell('Anapneo')
    anapneo.cast_spell()
    broom =Jinx('Broom')
    broom.cast_spell()
    maxima = Modifier('Maxima')
    maxima.cast_spell()