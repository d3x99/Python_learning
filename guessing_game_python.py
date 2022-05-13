guess_count = 0
secret_number = 9
guess_limit = 3

'''
while guess_count < guess_limit:
    guess = int(input("Guess number: "))
    if guess == secret_number:
        print('You won')
        break
    elif guess_count == 2:
        print('You lost')
        break
    else:
        guess_count = guess_count + 1
'''
# other option
while guess_count < guess_limit:
    guess = int(input("Guess number: "))
    guess_count += 1
    if guess == secret_number:
        print('You won')
        break

else:
    print('You lost')














