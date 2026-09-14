# D4: random & Module

import random
import my_module

#random integer from a to b, inclusively: random.randint(a, b)
random_integer=random.randint(1, 10)
print(random_integer)
# random choice
random_heads_or_tails = random.randint(0,1)
print(random_heads_or_tails)
if random_heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")

#random from 0 to 1 (doesn't include 1): random.random()
random_number_0_to_1=random.random()
random_number_0_to_10=random.random()*10
print(random_number_0_to_1)
print(f"{random_number_0_to_10:.02f}")

# import from another module
print(my_module.my_number)

