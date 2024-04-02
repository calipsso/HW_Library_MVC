from Model import DbLibraryOperations
from view import LibViewer

class LibController:
    def __init__(self):
        self.mLib = DbLibraryOperations()
        self.vLib = LibViewer()

    def add_Book(self, bookInfo):
        self.mLib.addBook(bookInfo)

    def add_User(self, userInfo):
        self.mLib.addUser(userInfo)

    def search_Book(self, searchInfo):
        self.mLib.searchBook(searchInfo)
    def menu(self):
        self.vLib.menu()