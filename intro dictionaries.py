customer = {
    'name': 'rajkumar',
    'age': 23,
    'is_verified': True
}

#print(customer['is_verified'])
#print(customer.get('Name', 'specified data is not there'))
print(customer.get('name', 'specified data is not there'))
customer['name'] = 'Raj Kumar M'
print(customer.get('name', 'specified data is not there'))
customer['DOB'] = '14_05_1999'              #TO ADD A DATA IN DICTIONARY
print(customer.get('DOB', 'specified data is not there'))
print(customer)
