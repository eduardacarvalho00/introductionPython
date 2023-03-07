from time import sleep

# WHILE - da suporte a um loop que executa um número desconhecido de vezes

user_input = ''
inputs = []

while user_input.lower() != 'done':
    if user_input:
        inputs.append(user_input)
    user_input = input('Enter a new value, or done when done: ')
print('ok, tanks :) aqui está seus inputs: ' + str(inputs))


# FOR - pode ser usado para interação em listas. usa com objetos iteráveis, em que você executará um loop por um número conhecido de vezes.

countdown = [4, 3, 2, 1, 0]
for number in countdown:  # se tiver mais de uma variavel, são separadas por vírgulas
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")
