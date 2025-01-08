import random
import hangman_words
import hangman_art


word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f'You have {lives} lives left')
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've alreay guessed {guess}")

    else:
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

    if guess not in chosen_word:
        print("You Chose a Wrong letter , You lost a Life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'The word was {chosen_word}')

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(hangman_art.stages[lives])