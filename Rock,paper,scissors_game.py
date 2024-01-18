from random import randint
first_pool = ((randint(1,3)),(randint(1,3)),(randint(1,3)))
second_pool = first_pool[randint(0,2)]
def game(figure = second_pool):
    if second_pool == 1:
        return ('rock')
    elif second_pool == 2:
        return('paper')
    else:
        return ('scissors')
choice = input("Please pick between rock, paper or scissors - ")
results = game()
def compute(game_choice = results, user_choice = choice):
    l = ('You lose')
    w = ('You win')
    if choice == results:
        return ('Its a tie')
    else:
        while choice != results:
            if choice == 'rock' and results == 'scissors':
                return (w)
            elif choice == 'rock' and results == 'paper':
                return (l)
            elif choice == 'paper' and results == 'rock':
                return(w)
            elif choice == 'paper' and results == 'scissors':
                return(l)
            elif choice == 'scissors' and results == 'rock':
                return(l)
            elif choice == 'scissors' and results == 'paper':
                return(w)
            else:
                return('There was an error')
print(compute())
next_round = input('Press q to quit and a to go again - ')
while next_round != 'q':
    first_pool = ((randint(1,3)),(randint(1,3)),(randint(1,3)))
    second_pool = first_pool[randint(0,2)]
    choice = input("Please pick between rock, paper or scissors - ")
    results = game()
    print(compute())
    next_round = input('Press q to quit and a to go again - ')
else:
    quit()