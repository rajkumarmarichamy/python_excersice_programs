x_list = range(5)
y_list = range(4)
total = 0
for x in x_list:
    for y in y_list:
        print(f'({x},{y})')
        total += 1
print(total)