class Ninja:
  def __init__( self, firstName, lastName, prizes, pet_food, pet ):
    self.firstName = firstName
    self.lastName = lastName
    self.prizes = prizes
    self.pet_food = pet_food
    self.pet = pet
  def walk(self):
    self.pet.play()
  def feed(self):
    self.pet.eat()
  def shower(self):
    self.pet.noise()
  

  