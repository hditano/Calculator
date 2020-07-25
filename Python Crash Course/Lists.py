Names = ['Hernan', 'Sebastian', 'Zoe', 'Gimena', 'Ricardo', 'Marta']

# message = f"Hello {Names[0]}. Por lo que se sos el hermano de {Names[1]}, el papa de {Names[2]},y tu esposa es {Names[-1]}"

message = f"Los Invito a mi cena a las siguientes personas {Names[0]}, {Names[1]}, {Names[2]}, {Names[3]}, {Names[4]}, {Names[5]}"
noPuedeVenir = 'Sebastian'

print(message)

message1 = f"Lamenablemente {Names[1]}, no puede venir a la cena"
print(message1)

Names.remove(noPuedeVenir)
Names.append('Run')
message2 = f"Pero viene {Names[-1]}"

print(message2)

message3 = f"Encontramos una mesa mas grande!!"
Names.insert(0, 'Enrique')
Names.insert(3, 'Marta Gutierrez')
Names.append('Romina')

message4 = f"La nueva lista es {Names}"

print(message3)
print(message4)

message5 = f"Lamentablemente tenemos mesa para 4 personas"
print(message5)
firstGuest = Names.pop(0)
message6 = f"Perdon {firstGuest}, la proxima sera"
print(message6)
secondGuest = Names.pop(2)
message7 = f"Perdon {secondGuest}, la proxima sera"
print(message7)
thirdGuest = Names.pop(-1)
message8 = f"Perdon {thirdGuest}, la proxima sera"
print(message8)

print(f"Ustedes siguen invitados, {Names[0]}, {Names[1]}, {Names[2]}, {Names[3]}, {Names[4]}, {Names[5]}")
print(len(Names))
print("Gracias por venir a la fiesta!!")
Names.remove('Zoe')
Names.remove('Run')
Names.remove('Gimena')
Names.remove('Ricardo')
Names.remove('Marta')
print(Names)


