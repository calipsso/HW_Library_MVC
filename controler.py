from Model import DbLibraryOperations
from view import LibViewer
class LibController:
    def __init__(self):
        self.mLib = DbLibraryOperations()
        self.vLib = LibViewer()

    def add_Book(self):
        self.mLib.addBook()

    def add_User(self, userInfo):
        self.mLib.addUser(userInfo)

    def menu(self):
        while True:
            print("Vyberte z menu:")
            print("1. Pridat knihu")
            print("2. Registracia uzivatela")
            print("3. Vyhladat knihu")
            vyber = int(input("zadaj volbu: "))

            if vyber == 1:
                self.mLib.addBook()
            elif vyber == 2:
                self.mLib.addUser()
            elif vyber == 3:
                self.vLib.searchBook()
            else:
                print("Neplatny vstup")
