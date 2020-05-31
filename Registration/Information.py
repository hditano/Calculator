from Registration import FileHelper, Users


class Information:

    def __init__(self, user, password):
        self.my_dict = {
            'a': self.add,
            'r': self.remove,
            'd': self.displayRecords,
            'c': self.changeUser,
            'q': quit}
        self._user = user
        self._password = password

    def displayInformation(self):
        my_display = FileHelper.Filehelper(self._user, self._password)
        print(f"Total Records: {my_display.totalRecords()}")
        print("[A]dd new Data | [R]emove Data | [D]isplay Records | [C]hange User | [Q]uit")
        value = input().lower()
        self.my_dict[value]()

    def add(self):
        my_add = FileHelper.Filehelper(self._user, self._password)
        my_add.add()

    def remove(self):
        my_remove = FileHelper.Filehelper(self._user, self._password)
        my_remove.remove()

    def changeUser(self):
        self._user = input("Please change your User (1) or (2): ")
        self._password = input("Type in your Password: ")
        my_user = Users.Data(self._user, self._password)
        my_user.chequeardatos()

    def displayRecords(self):
        my_display = FileHelper.Filehelper(self._user, self._password)
        my_display.displayRecords()

    def default(self):
        return "Incorrect Input"
