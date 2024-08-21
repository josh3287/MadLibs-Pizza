# This is random pizza topping generator
import random


style = {'New York', 'Chicago'}
cheese = {'Cheddar', 'Mozzarella', 'Gorgonzola', 'Provolone'}
friends = {'James', 'Robert', 'John', 'David', 'Mary', 'Patricia','Jennifer', 'Linda', 'Elizabeth' }
madlib = f"{friends}, {friends} and I have not seen each other in years. 
We love to go out to eat so I invited them to go get piza. 
{friends} likes {style} {cheese} pizza which has always been odd since I'm allergice to the type"

def decide_for_me():
    print("Welcome to MadLibs, a story randomizer")
    input("New York or Chicago style pizza: ")
    for friend in friends:
        return random.friends()
decide_for_me()