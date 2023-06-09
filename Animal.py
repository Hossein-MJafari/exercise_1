
class Animal:
    def __init__(self, name, age, weight, height, species):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.species = species
        self.food = None

    def set_food(self, food_name):
        self.food = food_name

    def move(self):
        return 'Moving...'

    def eat(self):
        print(f"{self.name} is eating {self.food.name}.")

    def communicate(self):
        return f"Hi...my name is {self.name}"

    def breed(self):
        pass

    def sleep(self):
        return f'{self.name} has fallen asleep...'


class mammals(Animal):
    def __init__(self, name, age, weight, height, species, fur_color, warmblooded:bool):
        super().__init__(name, age, weight, height, species)
        self.fur_color = fur_color
        self.warmblooded = warmblooded


class Dog(mammals):
    def __init__(self, name, age, weight, height, species, breed):
        super().__init__(name, age, weight, height, species)
        self.breed = breed
        self.sound = 'Woof'

    def bark(self):
        super().communicate()
        return self.sound


class Cat(mammals):
    def __init__(self, name, age, weight, height, species, breed):
        super().__init__(name, age, weight, height, species)
        self.breed = breed
        self.sound = 'Meow'

    def meow(self):
        super().communicate()
        return self.sound


class Horse(mammals):
    def __init__(self, name, age, weight, height, species, breed, manecolor):
        super().__init__(name, age, weight, height, species)
        self.breed = breed
        self.manecolor = manecolor

    def gallop(self):
        pass


class Cow(mammals):
    def __init__(self, name, age, weight, height, species, breed, milkproduction):
        super().__init__(name, age, weight, height, species)
        self.breed = breed
        self.milkproduction = milkproduction

    def moo(self):
        super().communicate()
        return 'Moooo...'


class Elephant(mammals):
    def __init__(self, name, age, weight, height, species, tuskLength, trunkLength):
        super().__init__(name, age, weight, height, species)
        self.tuskLength = tuskLength
        self.trunkLength = trunkLength

    def trumpet(self):
        super().communicate()
        return f'{self.name} is making the trumpet sound.'


class Birds(Animal):
    def __init__(self, name, age, weight, height, species, featherColor, beakType):
        super().__init__(name, age, weight, height, species)
        self.featherColor = featherColor
        self.beakType = beakType

    def fly(self):
        super().move()
        return 'Flying...'


class Eagle(Birds):
    def __init__(self, name, age, weight, height, species, featherColor, beakType, wingLength):
        super().__init__(name, age, weight, height, species, featherColor, beakType)
        self.wingLength = wingLength


class Penguin(Birds):
    def __init__(self, name, age, weight, height, species, featherColor, beakType, swimSpeed):
        super().__init__(name, age, weight, height, species, featherColor, beakType)
        self.swimSpeed = swimSpeed

    def slideOnBelly(self):
        super().fly()
        return "Wwwoooeeeeiiiii, I'm sliding on my belly on ice!"


class Parrot(Birds):
    def __init__(self, name, age, weight, height, species, featherColor, beakType):
        super().__init__(name, age, weight, height, species, featherColor, beakType)

    def mimicSound(self, sound):
        return f'{self.name} mimics {sound}.'


class Fish(Animal):
    def __init__(self, name, age, weight, height, species, coldBlooded:bool, scaleColor):
        super().__init__(name, age, weight, height, species)
        self.coldBlooded = coldBlooded
        self.scaleColor = scaleColor

    def swim(self):
        super().move()
        return 'Swimming...'


class Shark(Fish):
    def __init__(self, name, age, weight, height, species, coldBlooded, scaleColor):
        super().__init__(name, age, weight, height, species, coldBlooded, scaleColor)

    def hunt(self):
        return f'{self.name} just hunted a fish!'


class Salmon(Fish):
    def __init__(self, name, age, weight, height, species, coldBlooded, scaleColor):
        super().__init__(name, age, weight, height, species, coldBlooded, scaleColor)


class Reptiles(Animal):
    def __init__(self, name, age, weight, height, species, color):
        super().__init__(name, age, weight, height, species)
        self.color = color

    def shedSkin(self):
        return f'{self.name} is preparing its new skin!'


class Snake(Reptiles):
    def __init__(self, name, age, weight, height, species, color, venomous: bool):
        super().__init__(name, age, weight, height, species, color)
        self.venomous = venomous

    def slither(self):
        super().move()
        return f'{self.name} is slithering...'


class Lizard(Reptiles):
    def __init__(self, name, age, weight, height, species, color):
        super().__init__(name, age, weight, height, species, color)

    def regenerateTail(self):
        return f"ahh... {self.name}'s tail got cut again, regenerating..."


class Amphibian(Animal):
    def __init__(self, name, age, weight, height, species, skinType, metamorphisis: bool):
        super().__init__(name, age, weight, height, species,)
        self.skinType = skinType
        self.metamorphisis = metamorphisis

    def breathThroughSkin(self):
        return 'Who needs lungs?...when you can breath through your skin...'


class Frog(Amphibian):
    def __init__(self, name, age, weight, height, species, skinType, metamorphisis: bool, sound):
        super().__init__(name, age, weight, height, species, skinType, metamorphisis)
        self.sound = sound

    def jump(self):
        super().move()
        return f'{self.name} just jumped over there!'


class Habitat:
    def __init__(self, name, location, climate):
        self.name = name
        self.location = location
        self.climate = climate
        self.food = None
        self.animals = []
        self.is_clean = True

    def add_animal(self, name, age, weight, height, species):
        animal = Animal(name, age, weight, height, species)
        self.animals.append(animal)
        self.is_clean = False

    def set_food(self, food):
        self.food = food

    def clean(self):
        self.is_clean = True


class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


class CareTaker:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience
        self.animals = []

    def add_animal(self, name, age, weight, height, species):
        animal = Animal(name, age, weight, height, species)
        self.animals.append(animal)

    def feed_animal(self, food):
        for animal in self.animals:
            animal.set_food(food)

    def clean_habitat(self):
        for animal in self.animals:
            animal.habitat.clean()


# create objects
leaves = Food('Leaves', 100)
savannah = Habitat('Savannah', 'USA', 'hot-humid')
jane = CareTaker('Jane', 30, 'professional')

# add animal to habitat
savannah.add_animal('Giraffe', 5, 100, 4, 'southern-giraffe')

# add animal to caretaker
jane.add_animal('Lion', 4, 55, 1.5, 'cats')

# set food for habitat
savannah.set_food(leaves.name)
# set food for animal
giraffe = savannah.animals[0]
giraffe.set_food(leaves.name)

lion = jane.animals[0]
lion.set_food(leaves.name)

# caretaker feeds the animals
jane.feed_animal(leaves.name)

# another example
sea = Habitat("Caspian-Sea", "Iran", "cool-humid")
sea.add_animal('Mr.Shark', 5, 80, 1.8,'white-shark')
sea.set_food("fishes")


mrShark = Shark('Mr.Shark', 5, 80, 1.8,'white-shark', False, 'light-blue')
print(mrShark.hunt())
print(mrShark.communicate())