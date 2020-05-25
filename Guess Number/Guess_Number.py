import random

init = 0
result = 0
while init != 3:
    init = init + 1
    print(f"init es {init}")
    value = int(input("Eliga un numero que quiera: "))
    result = random.randint(1, 100)
    if result == value:
        print(f"Gano, el numero era {result}: ")
        break
    else:
        value = int(input("Eliga otro numero: "))
else:

    print(f"Perdio, el numero era {result}")
