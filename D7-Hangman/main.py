import random

word_list = ["python", "java", "javascript", "ruby", "html", "css", "csharp", "golang", "swift", "kotlin"]
lives=6

chosen_word = random.choice(word_list)
print(f"Chosen word is: {chosen_word}")
placeholder = ""
for letter in chosen_word:
    placeholder += "_"

game_over = False

correct_letters =[]

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            correct_letters.append("_")
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. Now you have {lives} lives left.")
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win!")