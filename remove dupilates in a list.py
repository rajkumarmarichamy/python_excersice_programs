numbers = [2,6,4,8,9,5,2,6]
uniques =[]

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)