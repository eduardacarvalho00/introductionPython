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
