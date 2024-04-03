from Model import DbConnection
from Model import DbLibraryOperations
from controler import LibController
from view import LibViewer

db_conn = DbConnection()
db_operations = DbLibraryOperations()
lib_viewer = LibViewer()
lib_controller = LibController()

lib_controller.menu()