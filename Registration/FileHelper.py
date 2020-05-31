from Registration import Information


class Filehelper:

    def __init__(self, user, password):
        self._user = user
        self._password = password

    def totalRecords(self):
        count = 0
        with open(self.path(self._user), 'r+') as file:
            totalRecords = file.readlines()
            for i in totalRecords:
                count += 1
        return count

    def add(self):
        try:
            with open(self.path(self._user), 'a+') as file1:
                file1.writelines(input("Please Type in your Text: ") + '\n')
        finally:
            my_add = Information.Information(self._user, self._password)
            my_add.displayInformation()

    def remove(self):
        try:
            with open(self.path(self._user), 'r') as file2:
                totalRecords = file2.readlines()
                for count, ele in enumerate(totalRecords, 1):
                    print(count, ele.strip())
                line_to_delete = int(input("Which line would you like to delete?"))
            with open(self.path(self._user), 'w') as file2:
                for line in totalRecords:
                    if line.strip("\n") != totalRecords[line_to_delete - 1]:
                        file2.write(line)
        finally:
            my_remove = Information.Information(self._user, self._password)
            my_remove.displayInformation()

    def displayRecords(self):
        with open(self.path(self._user), 'r') as file3:
            totalRecords = file3.readlines()
            for count, ele in enumerate(totalRecords, 1):
                print(count, ele.strip())
        my_display = Information.Information(self._user, self._password)
        my_display.displayInformation()

    def path(self, path):
        if path == "1":
            return "TextFile1.txt"
        if path == "2":
            return "TextFile2.txt"
        else:
            pass
