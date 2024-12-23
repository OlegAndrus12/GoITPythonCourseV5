class Monster:
    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        # REASON !!!!

    # methods
    def attack(self, amount):
        print("The monster has attacked!")
        print(f"{amount} damage was dealt")
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")


class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        # REASON !!!!
        super().__init__(**kwargs)

    def swim(self):
        print(f"The fish is swimming at a speed of {self.speed}")


class Shark(Monster, Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
        super().__init__(
            health=health, energy=energy, speed=speed, has_scales=has_scales
        )


shark = Shark(bite_strength=50, health=200, energy=55, speed=120, has_scales=False)

print(shark.speed, shark.health)
