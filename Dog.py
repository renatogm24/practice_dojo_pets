from Pet import Pet
class Dog(Pet):
  def __init__(self, name, type, candies, health, energy):
    super().__init__(name, type, candies, health, energy)
  def noise(self):
    print("Woof")