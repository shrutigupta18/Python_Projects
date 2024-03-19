import random
import hangman_stages

print("Let start Hangman Game!!!")
print(".......Begin the game........")      

word = ['Mayank','Shruti','Shubh','Manvi','Richa','Surshti','Charu','Rishu','Sammed']
lives = 6
select = random.choice(word)
#print(select)
display = []


for i in range(len(select)): #for letter in select:
    display += '_'
print(display)  
game_over = False
while not game_over:
    
    first = input("Guess a word\n")
    
    for position in range(len(select)):
        letter = select[position]
        if letter == first:
            display[position] = first 
    print(display)
    
    if (first not in select):
        lives -= 1

        if lives == 0:
            game_over = True
            print("You lose !!!")
    
    if ('_' not in display):
        game_over = True
        print('congratulations You Win the game!!!!')
    
    print(hangman_stages.stages[lives])    
    print(lives)
print(display)    
