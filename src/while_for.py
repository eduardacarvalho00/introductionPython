# WHILE - da suporte a um loop que executa um número desconhecido de vezes

user_input = ''
inputs = []

while user_input.lower() != 'done':
    if user_input:
        inputs.append(user_input)
    user_input = input('Enter a new value, or done when done: ')
print('ok, tanks :) aqui está seus inputs: ' + str(inputs))
