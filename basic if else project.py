#''' price of a house is 1M$
#if the buyer has good credit
#    they need to put down 10% downpayment
#otherwise
#    they need to put down 20% downpayment
#print the down payment'''

house_price = 1000000
print('scale your credit score in 1 to 10')

credit_score = int(input('>: '))
print('salary in multiple of lakhs')
salery = int(input('>: '))

if credit_score >= 6 and salery >= 2:
    print('your credit score and salary are good')
    print(f'your downpayment amount is {house_price * 0.1}')
elif credit_score >= 6 and not salery >= 2:
    print('your credit score is good but salary is not')
    print(f'your downpayment amount is {house_price * 0.2}')
elif not credit_score >= 6 and not salery >= 2:
    print('your credit score and salary is not good')
    print(f'your downpayment amount is {house_price * 0.5}') 