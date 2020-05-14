class Animal:
    weight_list = []
    weight_max = {'goose': 0, 'cow': 0, 'sheep': 0, 'chicken': 0, 'goat': 0, 'duck': 0, }
    def talk(self):
        return(print('The animal says', '"'+self.voice+'"'))
    def collect(self):
        return(print('You collected', self.product))
    def feed(self):
        return(print('You gave', self.food, 'to the animal'))
    def weights_sum(self):
        return(sum(Animal.weight_list))
    def maximum_weight(self):
        return(max(Animal().weight_max.items(), key=lambda x: x[1]))

class Goose(Animal):
    def __init__(self, name = None, weight = 10 ):
        self.name = name
        self.weight = weight
        self.product = 'meat'
        self.voice = 'shhhh'
        self.food = 'grass'
        Animal.weight_list.append(self.weight)
        if self.weight > Animal().weight_max['goose']:
            Animal().weight_max.update({'goose': self.weight})

class Cow(Animal):
    def __init__(self, name = None, weight = 350 ):
        self.name = name
        self.weight = weight
        self.product = 'milk'
        self.voice = 'mooo'
        self.food = 'hay'
        Animal.weight_list.append(self.weight)
        if self.weight > Animal().weight_max['cow']:
            Animal().weight_max.update({'cow': self.weight})

class Sheep(Animal):
    def __init__(self, name = None, weight = 50 ):
        self.name = name
        self.weight = weight
        self.product = 'fur'
        self.voice = 'baaaa'
        self.food = 'straw'
        Animal.weight_list.append(self.weight)
        if self.weight > Animal().weight_max['sheep']:
            Animal().weight_max.update({'sheep': self.weight})

class Chicken(Animal):
    def __init__(self, name = None, weight = 1 ):
        self.name = name
        self.weight = weight
        self.product = 'eggs'
        self.voice = 'quack'
        self.voice = 'cluck-cluck'
        self.food = 'grain'
        Animal.weight_list.append(self.weight)
        if self.weight > Animal().weight_max['chicken']:
            Animal().weight_max.update({'chicken': self.weight})

class Goat(Animal):
    def __init__(self, name = None, weight = 50 ):
        self.name = name
        self.weight = weight
        self.product = 'milk'
        self.voice = 'meeeee'
        self.food = 'leafs'
        Animal.weight_list.append(self.weight)
        if self.weight > Animal().weight_max['goat']:
            Animal().weight_max.update({'goat': self.weight})

class Duck(Animal):
    def __init__(self, name = None, weight = 4 ):
        self.name = name
        self.weight = weight
        self.product = 'eggs'
        self.voice = 'quack'
        self.food = 'bead'
        Animal.weight_list.append(self.weight)
        if self.weight > Animal().weight_max['duck']:
            Animal().weight_max.update({'duck': self.weight})

gees = [Goose(name = 'Серый'), Goose(name = 'Белый')]
cows = [Cow(name = 'Манька')]
sheeps = [Sheep(name ='Барашек'), Sheep(name = 'Кудрявый')]
chikens = [Chicken(name = 'Ко-ко'), Chicken(name = 'Кукареку')]
goats = [Goat(name = 'Рога'), Goat(name = 'Копыта')]
ducks = [Duck(name = 'Кряква')]

sheeps[0].talk()
goats[1].feed()
chikens[0].collect()

print('Общий вес животных:', Animal().weights_sum())
print('Самое большое животное:', Animal().maximum_weight())