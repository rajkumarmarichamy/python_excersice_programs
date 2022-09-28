# write a program to play a car game
# the car will start if you type start and stop if you type stop and quit to quit the game


started = False
while True:
    command = (input(':>')).upper()
    if command == 'START':
        if not started:
            print('the car is started')
            started = True
        else:
            print('the car is already started')
    elif command == 'STOP':
        if started:
            print('the car is stopped')
            started = False
        else:
            print('the car is alread stopped')
    elif command == 'QUIT':
        break
    else:
        print('unacceptabe command')