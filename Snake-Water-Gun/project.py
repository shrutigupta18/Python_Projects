import random
#snake water gun game


def game(Comp , you):
    if Comp == you:
        return None
    elif Comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif Comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif Comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

          
print("Comp Turn: Snake(s) Water(w) or Gun(g)? ")
randNo = random.randint(1, 3)
if randNo == 1:
    Comp = 's'
elif randNo == 2:
    Comp = 'w'
elif randNo == 3:
    Comp = 'g'

you = input("Your Turn: Snake(s) water(w) or gun(g)? ")

a = game(Comp , you)

print(f"Computer chose{Comp}\n")
print(f"you chose{you}\n")
if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")