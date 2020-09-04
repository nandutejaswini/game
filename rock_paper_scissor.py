import random
com=0
player=0
def user():
    user_selects=input("choose rock paper and scissor")
    if user_selects=="rock":
        print("rock")
    elif user_selects=="paper":
        print("paper")
    else:
        print("scissor")
    return user_selects
def computer():
    com_selects=random.randint(1,3)
    if com_selects==1:
        com_selects="rock"
    elif com_selects==2:
        com_selects="paper"
    else:
        com_selects="scissor"
    return com_selects
while True:
    user_selects = user()
    com_selects = computer()
    if user_selects == "rock":
        if com_selects == "scissor":
            print("you choose rock,computer choose scissor,you won")
            player += 1
        elif com_selects == "paper":
            print("you choose rock,computer choose paper,you won")
            player += 1
        elif com_selects == "rock":
            print(" both are win")

            
    elif user_selects == "paper":
        if com_selects == "scissor":
            print("you choose paper,computer choose scissor,computer won")
            com += 1
        elif com_selects == "rock":
            print("you choose paper,computer choose rock,you won")
            player += 1
        elif com_selects == "paper":
            print(" both are win")

    elif user_selects == "scissor":
        if com_selects == "rock":
            print("you choose scissor,computer choose rock,computer won")
            com += 1
        if com_selects == "paper":
            print("you choose scissor,computer choose paper,player won")
            player += 1
        elif com_selects == "scissor":
            print(" both are win")

    print("computer: ",com)
    print("player:",player)
    print("if u want to continue choose y/n")
    s = input()
    if s == 'y':
        pass
    else:
        break

