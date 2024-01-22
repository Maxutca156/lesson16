import json

person = {
    'name': 'Max',
    'age': 10,
    'phones': ['9111', '738333']
}
result = json.dumps(person)
print(result)
print(type(result))

my_wallet = {'money': 12345, 'currency': 'Рубли', 'name': 'Arkady'}
result = json.dumps(my_wallet)
print(result)
print(type(result))