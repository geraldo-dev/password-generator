from random import choices


letters = ['a','b','c','d','e','f','g','h','i','j']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
symbols = ['@','_','#','.']

#uni todas as listas
new_list = letters + numbers + symbols

def new_password():
    _password = ''
    for x in range(8):
        item = choices(new_list)
        _password = f'{_password}{item[0]}'
    return _password

while True:
    generate_password = input('quer gera uma nova senha sim ou não: ')

    if generate_password == 'sim' or generate_password == 's':
        print(new_password())
    elif generate_password == 'nao' or generate_password == 'n':
        break
    else:
        print('ops ... opição invalida')