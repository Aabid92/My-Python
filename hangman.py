import random 

word_list = ["apple", "lollipop", "android"]


chosen_word = random.choice(word_list)

print(f"chosen word is {chosen_word}")


display = []
word_len = len(chosen_word)

for _ in range(word_len):
    display += "_"
print(display)     

end_of_game = False
while not end_of_game :
    guess = input("guess a latter: ").lower()

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("your win")


