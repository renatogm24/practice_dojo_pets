class Pet:
  def __init__( self, name, type, candies, health, energy ):
    self.name = name
    self.type = type
    self.candies = candies
    self.health = health
    self.energy = energy
  def sleep(self):
    self.energy += 25
    print(f"Energy:{self.energy}")
    print(f"Health:{self.health}")
  def eat(self):
    self.energy += 5
    self.health += 10
    print(f"Energy:{self.energy}")
    print(f"Health:{self.health}")
  def play(self):
    self.health += 5
    print(f"Energy:{self.energy}")
    print(f"Health:{self.health}")
  def noise(self):
    print("Noise")