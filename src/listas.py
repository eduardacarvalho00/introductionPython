# LISTAS

planets = ["Mercury", "Venus", "Earth", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]


number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")
# There are 8 planets in the solar system


# Adicionar valores ás lista
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")
# There are actually 9 planets in the solar system.

# remover valores ds listas
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets,
      "planets in the solar system.")

# Índices negativos
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])
# The last planet is Neptune
# The penultimate planet is Uranus


jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
# Jupiter is the 5 planet from the sun


# min e max
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650  # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is",
      bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is",
      bus_weight * max(gravity_on_planets), "kg")
# On Earth, a double-decker bus weighs 12650 kg
# The lightest a bus would be in the solar system is 4769.05 kg
# The heaviest a bus would be in the solar system is 29854 kg


# cortar listas
planets_before_earth = planets[0:2]
print(planets_before_earth)
# ['Mercury', 'Venus']

numbers_list = [2, 91, 38, 2, 9, 0]
planets_sorted = numbers_list.sort()
print(numbers_list.sort())
