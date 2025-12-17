import random

def validate_user_input(value):
    while True:
        if value.casefold() in ('p', 'r', 's'):
            return value
        else:
            print('Please enter valid input!')
            value = input('Rock, Paper, or Scissors? (r/p/s): ')

def random_choice():
    random_number = random.randint(1, 3)
    match(random_number):
        case 1:
            return 'r'
        case 2:
            return 'p'
        case 3:
            return 's'

def choice_symbol(choice):
    match(choice):
        case 'p':
            return '📃'
        case 'r':
            return '🪨'
        case 's':
            return '✂️'

def game_logic(user_cho, computer_cho):
    if user_cho == 'p' and computer_cho == 'r':
        return 'You win'
    elif user_cho == 'r' and computer_cho == 's':
        return 'You win'
    elif user_cho == 's' and computer_cho == 'p':
        return 'You win'
    elif user_cho == computer_cho:
        return 'Draw'
    else:
        return 'You loss'

def run_game():
    while True:
        user_choice = input('Rock, Paper, or scissors? (r/p/s): ')
        user_choice = validate_user_input(user_choice)
        computer_choice = random_choice()
        print(f'Your choice {choice_symbol(user_choice)}')
        print(f'Computer choice {choice_symbol(computer_choice)}')
        print(game_logic(user_choice, computer_choice))
        cont = input('Continue? (y/n): ')
        if cont.lower() == 'n':
            break

run_game()