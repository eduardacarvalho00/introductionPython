# FUNÇÃO PRINT
import sys
from datetime import date
print("show this is the console")


# VARIÁVEIS
sum = 1 + 2  #  3
product = sum * 2
print(product)


# TIPOS DE DADOS
planets_in_solar_system = 8  #  int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367  #  float, lightyears
can_liftoff = True  # boolean
shuttle_landed_on_the_moon = "Apollo 11"  # string

print(type(distance_to_alpha_centauri))


# DATAS
date.today()
print(date.today())
print("Today's date is: " + str(date.today()))


# ENTRADA DE USUARIO

print("Welcome to the greeter program")
name = input("Enter your name ")
print("Greetings: " + name)


# TRABALHANDO COM NÚMEROS

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(int(first_number) + int(second_number))


# LÓGICA BOOLIANA EM PYTHON

a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)

c = 20
d = 10
if c >= d:
    print("a is greater than or equal to b")
elif c == d:
    print("a is equal to b")


# LÓGICA CONDICIONAL ANINHADA

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print("a is greater than b and b is greater than c")
    else:
        print("a is greater than b and less than c")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")


# OPERADORES BOOLEANOS AND - OR

a = 23
b = 34
# para que a expressão seja True, pelo menos uma das subexpressões deve ser verdadeira.
if a == 34 or b == 34:
    print(a + b)


a = 23
b = 34
# As duas condições na expressão de teste devem ser verdadeiras para que a expressão de teste inteira seja avaliada como True.
if a == 34 and b == 34:
    print(a + b)


# MÉTODOS DE CADEIA DE CARACTERES

heading = "temperatures and facts about the moon"
heading.title()
'Temperatures And Facts About The Moon'


# DIVIDIR UMA CADEIA DE CARACTERES

temperatures = """Daylight: 260 F
... Nighttime: -280 F"""
temperatures .split()
['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']

temperatures .split('\n')
['Daylight: 260 F', 'Nighttime: -280 F']


# PESQUISAR UMA CADEIRA DE CARACTERES

"Moon" in "This text will describe facts and challenges with space travel"
False
"Moon" in "This text will describe facts about the Moon"
True


temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
temperatures.find("Moon")
-1
temperatures.find("Mars")
65

temperatures.count("Mars")
1
temperatures.count("Moon")
0

"The Moon And The Earth".lower()
'the moon and the earth'
"The Moon And The Earth".upper()
'THE MOON AND THE EARTH'


# VERIFICAR CONTEÚDO
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
['Mars average temperature', ' -60 C']
parts[-1]
' -60 C'

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
30

"-60".startswith('-')
True
if "30 C".endswith("C"):
    print("This temperature is in Celsius")
'This temperature is in Celsius'


# TEXTO DE TRANSFORMAÇÃO
"Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace(
    "Celsius", "C")
'Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C.'


text = "Temperatures on the Moon can vary wildly."
"temperatures" in text
False
"temperatures" in text.lower()
True

moon_facts = [
    "The Moon is drifting away from the Earth.",
    "On average, the Moon is moving about 4cm every year"
]
'\n'.join(moon_facts)
'The Moon is drifting away from the Earth.\nOn average, the Moon is moving about 4cm every year'
