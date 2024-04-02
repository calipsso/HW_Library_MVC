from Model import DbLibraryOperations
#from controler import LibController
class LibViewer:
    def __init__(self):
        self.mLib = DbLibraryOperations()
        #self.cLib = LibController()

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
            bookInfo = input("Zadaj: title, author_id, genre_id, ISBN, publication_year, copies: ")
            self.mLib.addBook(bookInfo)

