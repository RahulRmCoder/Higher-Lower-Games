from art import logo, vs
from game_data import data
import random

def formataccount(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f'{account_name}, {account_description}, {account_country}'

def checkscores(user_input,account1,account2):
    if account1>account2:
        return user_input=='a'
    else:
        return user_input == 'b'

print(logo)
score=0
game_continue=True
account_b= random.choice(data)

while game_continue:

    account_a=account_b
    account_b=random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f'Compare A: {formataccount(account_a)}')
    print(vs)
    print(f'Against B: {formataccount(account_b)}')

    account_count_a = account_a['follower_count']
    account_count_b = account_b['follower_count']

    guess = input("Who has more followers in Instagram? Type 'A' or 'B':").lower()

    is_correct = checkscores(guess,account_count_a,account_count_b)

    print('\n' * 20)
    print(logo)

    if is_correct:
        score+=1
        print(f'You right! Current score: {score}')
    else:
        print(f"You're wrong! Final score {score}")
        game_continue=False






