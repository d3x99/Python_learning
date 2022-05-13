user_input = ''
car_started = False
while True:
    user_input = input('>').lower()
    if user_input == str('start'):
        if car_started:
            print('Car is already started')
        else:
            car_started = True;
            print('Car started...')

    elif user_input == str('stop'):
        if not car_started:
            print('Car is already stopped')
        else:
            print('Car stopped...')
            car_started = False
    elif user_input == str('help'):
        print('''start - to start the car
stop - to stop the car
quit - to exit ''')
    elif user_input == str('quit'):
        break
    else:
        print('i dont understand')

