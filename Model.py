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
        return self.cursor.fetchall()

    def CloseConnection(self):
        self.conn.close()

class DbLibraryOperations:
    def __init__(self):
        self.db_connection = DbConnection()

    def addBook(self):
        print("Vlozte nozov knihy: ")
        title = input()
        print("Vlozte ISBN: ")
        ISBN = input()
        print("Vlozte Author ID")
        autID = input()
        print("Vlozte Genre ID")
        genID = input()
        print("Kopie")
        copies = input()
        add = "INSERT INTO books (title,author_id, genre_id, ISBN, copies) VALUES (%s, %s, %s, %s, %s)"
        parameters = title,autID, genID, ISBN, copies
        return self.db_connection.ExecQuery(add, parameters)
    def searchBook(self, searchInfo):
        search = ("SELECT title, author_id, genre_id from books WHERE title = %s", (searchInfo, ))
        return self.db_connection.ExecQuery(search)
    def addUser(self, userInfo):
        addUsr = ("INSERT INTO members (first_name, last_name, email, registration_date) VALUES (%s, %s, %s, %s)",(userInfo, ))
        return self.db_connection.ExecQuery(addUsr)

    def checkUsr(self, checkInfo):
        search = ("SELECT * from members WHERE first_name = %s ", (checkInfo))
        return self.db_connection.ExecQuery(search)