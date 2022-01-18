from Ninja import Ninja
#from Pet import Pet
from Dog import Dog
from Cat import Cat

pet1 = Cat("Andy","cat","tuna",100,100)
ninja1 = Ninja("Renato","Garay","Best Pet owner","croquettes",pet1)

pet2 = Dog("Dogandy","dog","croquette",100,100)
ninja2 = Ninja("Vanessa","Lopez","Best Pet owner","croquettes",pet2)

ninja1.feed()
ninja1.walk()
ninja1.shower()
ninja2.shower()