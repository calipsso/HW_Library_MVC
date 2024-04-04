import psycopg2

class DbConnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="b81s1xhecmfxnpmteb27",
            user="urici3i0icy8cuufham5",
            password="FrtbL6FqnCsROZMWocDBkgoOeoZC7R",
            host="b81s1xhecmfxnpmteb27-postgresql.services.clever-cloud.com",
            port="50013"
        )
        self.cursor = self.conn.cursor()
    def ExecQuery(self, query, parameters):
        self.cursor.execute(query, parameters)
        self.conn.commit()
    def searchQuery(self, query, parameters):
        self.cursor.execute(query, parameters)
        print(self.cursor.fetchall())
    def showQuery(self, query):
        self.cursor.execute(query)
        db = self.cursor.fetchall()
        for item in db:
            print(f"ID: {item[0]}, : {item[1]}")
    def CloseConnection(self):
        self.conn.close()
class DbLibraryOperations:
    def __init__(self):
        self.db_connection = DbConnection()
    def getUsrInput(self, prompt):
        print(prompt)
        return input()

    def addBook(self):
        title = self.getUsrInput("Vlozte nazov knihy: ")
        ISBN = self.getUsrInput("Vlozte ISBN knihy: ")
        autID = self.getUsrInput("Vlozte autora knihy: ")
        genID = self.getUsrInput("Vlozte zaner knihy: ")
        copies = self.getUsrInput("Vlozte mnozstvo kopii: ")
        add = "INSERT INTO books (title,author_id, genre_id, ISBN, copies) VALUES (%s, %s, %s, %s, %s)"
        parameters = title,autID, genID, ISBN, copies
        return self.db_connection.ExecQuery(add, parameters)
    def delBook(self):
        bookId = self.getUsrInput("Zadaj ID knihy")
        add = "DELETE FROM books WHERE book_id = %s "
        parameters = (bookId, )
        return self.db_connection.ExecQuery(add, parameters)
    def addUser(self):
        meno =self.getUsrInput("Vloz meno: ")
        priezvisko = self.getUsrInput("Vloz priezvisko: ")
        email = self.getUsrInput("email: ")
        addUsr = "INSERT INTO members (first_name, last_name, email) VALUES (%s, %s, %s)"
        parameters = meno, priezvisko,email
        return self.db_connection.ExecQuery(addUsr, parameters)
