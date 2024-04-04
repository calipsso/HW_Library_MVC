from Model import DbLibraryOperations
from view import LibViewer
class LibController:
    def __init__(self):
        self.mLib = DbLibraryOperations()
        self.vLib = LibViewer()

    def aplikacia_kniznica(self):
        while True:
            print("Vyberte z menu:")
            print("1. Pridat knihu")
            print("2. Registracia uzivatela")
            print("3. Vyhladat knihu")
            print("4. Vyhladat uzivatela")
            print("5. Vymazat knihu")
            vyber = int(input("zadaj volbu: "))

            if vyber == 1:
                print("Autory")
                self.vLib.showAuthor()
                print("---------------- \n Zanre ")
                self.vLib.showGenre()
                self.mLib.addBook()
            elif vyber == 2:
                self.mLib.addUser()
            elif vyber == 3:
                self.vLib.searchBook()
            elif vyber == 4:
                self.vLib.searchUsr()
            elif vyber == 5:
                self.vLib.showBooks()
                self.mLib.delBook()
            else:
                print("Neplatny vstup")
