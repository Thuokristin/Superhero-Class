class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self.secret_identity = secret_identity
        self.power_level = power_level
        self.is_flying = False

    def reveal_identity(self):
        print(f"By day, I am known as {self.secret_identity}!")

    def use_power(self):
        print(f"{self.name} unleashes their incredible power!")

    def fly(self):
        self.is_flying = True
        print(f"{self.name} takes to the skies!")

    def land(self):
        self.is_flying = False
        print(f"{self.name} gracefully lands.")

    def display_stats(self):
        print(f"--- {self.name} ---")
        print(f"Secret Identity: {self.secret_identity}")
        print(f"Power Level: {self.power_level}")
        print(f"Currently Flying: {self.is_flying}")

# Inheriting from Superhero to create a more specialized hero
class FlyingSuperhero(Superhero):
    def __init__(self, name, secret_identity, power_level, flight_speed):
        super().__init__(name, secret_identity, power_level)
        self.flight_speed = flight_speed

    # Override the use_power method to include flight-related actions
    def use_power(self):
        print(f"{self.name} soars through the air with a speed of {self.flight_speed}!")

    # Enhance the display_stats method
    def display_stats(self):
        super().display_stats()
        print(f"Flight Speed: {self.flight_speed}")

# Creating instances of our classes
superman = Superhero("Superman", "Clark Kent", "Over 9000!")
wonder_woman = FlyingSuperhero("Wonder Woman", "Diana Prince", "God-like", "Mach 2")

superman.reveal_identity()
superman.fly()
superman.use_power()
superman.land()
superman.display_stats()
print("\n")
wonder_woman.reveal_identity()
wonder_woman.use_power()
wonder_woman.display_stats()