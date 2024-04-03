from Model import DbLibraryOperations
#from view import LibViewer

class LibController:
    def __init__(self):
        self.mLib = DbLibraryOperations()
        #self.vLib = LibViewer()

    def add_Book(self):
        self.mLib.addBook()

    def add_User(self, userInfo):
        self.mLib.addUser(userInfo)

    def search_Book(self, searchInfo):
        self.mLib.searchBook(searchInfo)

    def menu(self):
        while True:
            print("Vyberte z menu:")
            print("1. Pridat knihu")
            print("2. Registracia uzivatela")
            print("3. Vyhladat knihu")
            try:
                vyber = int(input("zadaj volbu: "))
                break
            except:
                print("zadavaj len cisla")
        if vyber == 1:
            self.mLib.addBook()
