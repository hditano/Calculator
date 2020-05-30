from Registration import Users

while True:
    print("Welcome to the Registration System")
    eleccion = input("Please choose and User (1) or (2): ")
    password = input("Please Type in your Password: ")
    chequear = Users.Data(eleccion, password)
    chequear.chequeardatos()
    if eleccion is None and password is None:
        continue
    break

