# D5: Loops
## Ex1: elements in for loops
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


## Ex2: sum
student_score = [78, 65, 89, 86, 55, 91, 64, 89]
### Method1: sum()
sum_score = sum(student_score)
### Method2: for loop
sum_score2 = 0
for score in student_score:
    sum_score2 += score
print(f"Sum of scores is: {sum_score2}")

## Ex3: Max
### Method 1: max()
max_score1 = max(student_score)
### Methods 2: for loop
max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print(f"Max score is: {max_score}")        

