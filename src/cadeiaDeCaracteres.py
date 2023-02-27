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
