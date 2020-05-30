from Registration import Information


class Data:
    # Fields
    def __init__(self, user, password):
        self._user = user
        self._password = password

    @property
    def password(self, _password):
        return self._password

    @password.setter
    def password(self, new_password):
        pass

    def chequeardatos(self):
        if self._user == "1" and self._password == "123" or self._user == "2" and self._password == "3030":
            print(f"Welcome User {self._user}")
            print("Checking Data...Please Hold on")
            print("Access Granted....")
            my_info = Information.Information(self._user, self._password)
            my_info.displayInformation()

        else:
            print("Incorrect User...quiting program")
