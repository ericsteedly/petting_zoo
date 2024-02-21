from datetime import date
from crawling import Arachnid, Frog, Lizard, Snake, Turtle
from swimming import Duck, Fish, Swan, Gator, Goose
from walking import Llama, Goat, Horse, Pig, Donkey


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning")
jim = Pig("Jim", "pot-belly pig", "morning")
joe = Goat("Joe", "Billy Goat", "midday")
jill = Donkey("Jill", "standard donkey", "midday")
indie = Horse("Indie", "quarter-horse", "afternoon")

sarah = Snake("Sarah", "python")
sam = Lizard("Sam", "Salamander")
soren = Arachnid("Soren", "Scorpion")
santo = Frog("Santo", "poison dart frog")
slim = Turtle("Slim", "giant tortoise")

roy = Swan("Roy", "black swan")
rowdy = Goose("Rowdy", "canadian goose")
rhonda = Gator("Rhonda", "caiman")
rufus = Fish("Rufus", "goldfish")
ricardo = Duck("Ricardo", "mallard")

print(f'{indie.name} the {indie.species} is available to pet during the {indie.shift} shift.')



