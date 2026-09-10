# D4:List
import random

friends =["John", "Mary", "Bob", "Alice"]
# op. 1: random.choice() - returns a random element from a list
random_friend = random.choice(friends)
print(random_friend)
# op. 2: random.randint() - returns a random index from the list
random_integer = random.randint(0, len(friends)-1)
print(friends[random_integer])

# Nested list
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0][1]) # banana