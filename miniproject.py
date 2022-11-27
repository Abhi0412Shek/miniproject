import random


user_input = input("choose rock, paper, scissors")

computer_action = random.randint(1,3)
if computer_action==1:
    computer_action="rock"
elif computer_action==2:
    computer_action="paper"
elif computer_action==3:
    computer_action="scissors"  

print("computer choose :",computer_action)          

if user_input==computer_action:
    print(" the match was tied")
elif computer_action=="rock":
    if user_input =="paper":
        print("you win! paper covers rock")
    elif user_input=="scissors":
        print("you lose..rock smaches scissors")
elif computer_action=="paper":
    if user_input=="scissors":
        print("you win! scissors cuts paper")
    elif user_input=="rock":
        print("you lose.. paper covers rock")                
    

  