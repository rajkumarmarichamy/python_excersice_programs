def greet_user():
    print('Hi there!')
    print('Welcome aboard')


def greet_user_with_name(first_name, last_name):
    print(f'hi {first_name} {last_name} ')
    print('Welcome aboard')


def square(number):
    return number * number




print('start')
#greet_user()
greet_user_with_name('raj', 'kumar')   #positional arguments
greet_user_with_name(last_name='kumar', first_name='raj') #key word arguments
print('finish')

result = square(8)
print(result)
