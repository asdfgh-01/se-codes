import random
print("welcome to guess the word!")
game_dict = {
    "colors" : ["beige","pink","ruby","jade","ebony","olive","ivory"],
    "fruits" : ["apple","pineapple","strawberry","mango","orange","dragonfruit"],
    "flowers" : ["azalea","orchid","pansy","hyacinth","lavender","honeysuckle"],
    "animals" : ["cat","dog","panda","snake","wolf","rabbit"]
}
game_keys = []
for keys in game_dict:
    game_keys.append(keys)

flag1 = True
while flag1:
    r_key = random.randint(0,3)
    game_category = game_keys[r_key]
    r_value = random.randint(0,5)
    game_word = game_dict[game_category][r_value]
    blank_word = []
    for letter in game_word:
        blank_word.append('-')
    
    print(f"guess a {len(game_word)} word from the following category :{game_category}")
    guess = ''
    guess_count = 0
    while guess!=game_word:
        print("".join(blank_word))
        guess = input("enter your guess :")
        guess_count+=1
        if guess==game_word:
            print(f"congratulations! you have guessed the word in {guess_count} tries!")
            break
        elif len(blank_word)==guess_count:
            blank_word[blank_word.index('-')]=game_word[blank_word.index('-')]
            word = "".join(blank_word)
            print(f"you are out of guesses!\nthe word was {word}!\nbetter luck next time!")
            break
        else:
            print("this guess is not correct! let us reveal a letter to help!")
            flag2 = True
            while flag2:
                letter_index = random.randint(0,len(game_word)-1)
                if blank_word[letter_index]=='-':
                    blank_word[letter_index]=game_word[letter_index]
                    flag2 = False
    if(input("would you like to play again?")=='n'):
        flag1 = False

print("Thank you for playing!")