# guess the secret number in three trails to win or you lose

secret_number = 10
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count += 1
    if guess == secret_number:
        print('you win')
        break
else:
    print('you lose')