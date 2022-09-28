numbers_to_words = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}
phone_number = input('phone:> ')
phone_number_to_words = ''
for numbers in phone_number:
    phone_number_to_words += numbers_to_words[numbers] + ' '
print(phone_number_to_words)