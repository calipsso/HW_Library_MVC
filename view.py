from Model import DbConnection
from Model import DbLibraryOperations
class LibViewer:
    def __init__(self):
        self.db_connection = DbConnection()
        self.mLib = DbLibraryOperations()
    def searchBook(self):
        id = self.mLib.getUsrInput("Vlozte nazov knihy: ")
        search = "SELECT title FROM books WHERE book_id = %s"
        parameter = id
        return self.db_connection.searchQuery(search, parameter)



