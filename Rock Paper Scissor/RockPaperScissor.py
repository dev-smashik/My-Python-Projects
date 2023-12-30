import random

def game():
    User = input("What you want to pick? \
        \n1. Rock - 'r' \
        \n2. Paper - 'p' \
        \n3. Scissor - 's' \
        \nSelect your option: ")

    Computer = random.choice(['r', 'p', 's'])

    if User == Computer:
        return f"{User} == {Computer} - Match Tie! Try again"

    if win_game(User, Computer):
        return f"{User} > {Computer} - You won this game!"

    return f"{User} < {Computer} - You lost this match! Try again"


def win_game(User, Computer):
    if (User == 'r' and Computer == 's') or \
       (User == 's' and Computer == 'p') or \
       (User == 'p' and Computer == 's'):
       return True

print(game())