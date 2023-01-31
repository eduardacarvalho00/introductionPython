# FUNÇÃO PRINT
from math import ceil, floor
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


# MÉTODOS DE CADEIA DE CARACTERES <<<<<<<<<<<

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


# FORMATAÇÃO DO SINAL DE PORCENTAGEM

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" %
      mass_percentage)
'On the Moon, you would weigh about 1/6 of your weight on Earth'

print("""Both sides of the %s get the same amount of sunlight,
... but only one side is seen from %s because
... the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))


# .format() usa chaves ({}) como espaços reservados em uma cadeia de caracteres e usa a atribuição de variável para substituir o texto.
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(
    mass_percentage))
'On the Moon, you would weigh about 1/6 of your weight on Earth'


print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))
'You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earthc'

print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
'You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth'


# cadeias de caracteres f

print(
    f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
'On the Moon, you would weigh about 1/6 of your weight on Earth'

print(
    f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")
'On the Moon, you would weigh about 16.7% of your weight on Earth'


# USAR OPERAÇÕES MATEMÁTICAS

seconds = 1042
display_minutes = 1042 // 60  # arredondar para baixo usando a função piso //.
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)
# Output:
# 17
# 22

print(abs(39 - 16))
print(abs(16 - 39))
# Output
# 23
# 23

print(round(14.5))
# Output: 15


round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# Output
# 13
# 12
