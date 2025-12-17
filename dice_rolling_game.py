import random

count = 0
while True:
    choice = input('Roll the dice? (y,n): ').lower()
    if choice == 'y':
        num = int(input('How many you want to Roll the dice: '))
        for _ in range(num):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f'({die1}, {die2})')
            count += 1
    elif choice == 'n':
        print(f'The number of rolling the dice in this session is: {count}')
        print(f'Thanks for playing!')
        break
    else:
        print(f'Invalid input!')