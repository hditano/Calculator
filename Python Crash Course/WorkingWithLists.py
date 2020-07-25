# Usando For Loop en una lista

Pizzas = ['peperoni', 'fugazzeta', 'morron', 'margarita', 'anchoas']
for pizza in Pizzas:
    print(f'Mis Pizzas favoritas son {pizza}')
print('Me encanta la Pizza es una de mis comidas favoritas')

# Trabajando con Cubes

for value in range(1,11):
    print(value)

newList = [value for value in range(1,1000001)]
print(newList)
print(min(newList))
print(max(newList))
print(sum(newList))

cubes = []
for value in range(1,10):
    cube = value**3
    cubes.append(cube)
print(cubes)


# Slicing

print(f'The first three items in the list are: {Pizzas[0:3]}')
print(f'The last three items in the list are: {Pizzas[2:]}')

friends_pizza = Pizzas[:]

Pizzas.append('Naranja')
friends_pizza.append('tomate')

print('My Favourite Pizzas are: ')
for value in Pizzas:
    print(value)

print('My Friend\'s favourite pizzas are: ')
for value in friends_pizza:
    print(value)

# Tuples

print('Tuples')
foods = ('Milanesa', 'pollo', 'salchicas', 'carne', 'pollito')
for food in foods:
    print(food)

print('New Menu')
foods = ('Pasta', 'Sandwich', 'salchicas', 'carne', 'pollito')
for food in foods:
    print(food)
