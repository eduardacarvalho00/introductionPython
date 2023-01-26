# TRABALHANDO COM A SAÍDA

# função print
import sys
from datetime import date
print("show this is the console")


# variáveis
sum = 1 + 2  #  3
product = sum * 2
print(product)


# tipos de dados
planets_in_solar_system = 8  #  int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367  #  float, lightyears
can_liftoff = True  # boolean
shuttle_landed_on_the_moon = "Apollo 11"  # string

print(type(distance_to_alpha_centauri))


# datas
date.today()
print(date.today())
print("Today's date is: " + str(date.today()))


# entrada do usuário

print("Welcome to the greeter program")
name = input("Enter your name ")
print("Greetings: " + name)


# trabalhando com numeros

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(int(first_number) + int(second_number))


# lógica booliana em python

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


#  lógica condicional aninhada

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


# operadores boolianos and e or.

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
