from datetime import timedelta, datetime

def rocket_parts():
    return "payload, propellant, structure"

#Se você precisar usar o valor de uma função, essa função deverá retornar esse valor explicitamente. Caso contrário, será retornado None.

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24
print(round(days_to_complete(238855, 75)))



# parametros de palavra chave
def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")
print(arrival_time())
print(arrival_time(hours=0))

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

def variable_length(*args):
    print(args)

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

def crew_members(**kwargs):  # parametros de palavra chave
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")