from Model import DbConnection
from Model import DbLibraryOperations
class LibViewer:
    def __init__(self):
        self.db_connection = DbConnection()
        self.mLib = DbLibraryOperations()
    def searchBook(self):
        id = self.mLib.getUsrInput("Vloz ID knihy: ")
        search = "SELECT title, ISBN, publication_year FROM books WHERE book_id = %s"
        parameter = (id, )
        return self.db_connection.searchQuery(search, parameter)
    def searchUsr(self):
        priezvisko = self.mLib.getUsrInput("Zadaj priezvisko uzivatela: ")
        search = ("SELECT * from members WHERE last_name = %s ")
        parameters = (priezvisko, )
        return self.db_connection.searchQuery(search, parameters)
    def showBooks(self):
        show = "SELECT book_id, title FROM books"
        return self.db_connection.showQuery(show)
    def showAuthor(self):
        show = "SELECT author_id, name FROM authors"
        return self.db_connection.showQuery(show)
    def showGenre(self):
        show = "SELECT genre_id, name FROM genres"
        return self.db_connection.showQuery(show)
    def showUsr(self):
        show = "SELECT member_id, last_name FROM members"
        return self.db_connection.showQuery(show)



