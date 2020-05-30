class Filehelper:

    def __init__(self, user):
        self._user = user

    def totalRecords(self):
        count = 0
        with open(self.path(self._user)) as file:
            totalRecords = file.readlines()
            for i in totalRecords:
                count += 1
        return count

    def add(self):
        try:
            with open(self.path(self._user), 'a') as file:
                file.writelines(input("Please Type in your Text: "))
        except:
            print("No text, please try again")

    def remove(self):
        try:
            with open(self.path(self._user)) as file:
                totalRecords = file.readlines()
                for i in totalRecords:
                    print(f"{i}")
        except FileNotFoundError:
            print(f"Not {file} has been found")

    def path(self, path):
        if path == "1":
            return "TextFile1.txt"
        if path == "2":
            return "TextFile2.txt"
        else:
            pass
