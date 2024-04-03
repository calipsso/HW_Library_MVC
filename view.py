from Model import DbConnection
from Model import DbLibraryOperations
class LibViewer:
    def __init__(self):
        self.db_connection = DbConnection()
        self.mLib = DbLibraryOperations()
    def searchBook(self):
        print("Zadajte ID knihy")
        id = input()
        search = "SELECT title FROM books WHERE book_id = %s"
        parameter = id
        return self.db_connection.searchQuery(search, parameter)

