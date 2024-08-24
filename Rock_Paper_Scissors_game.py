import random

def get_choices():
    players_choice = input('Choose one (rock, paper, scissors):')
    comp = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(comp)
    saylaw = {'player': players_choice, 'computer': computer_choice}
    return saylaw
    
def winner(player, computer):
    print(f'Your chose {player}, computer choice {computer}')
    
    if player == computer:
        return 'Equal'
        
    elif player == "scissors":
        if computer == "paper":
            return "player wins"
        else:
            return "computer wins"
    
    elif player == "rock":
        if computer == "scissors":
            return "player wins"
        else:
            return "computer wins"
        
    elif player == "paper":
        if computer == "rock":
            return "player wins"
        else:
            return "computer wins"
        
choice = get_choices()

result = winner(choice['player'], choice['computer'])
print(result)