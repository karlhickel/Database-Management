import sqlite3
con = sqlite3.connect("StudentDataBase.db")
cursor = con.cursor()

class Menu:
    def Menu(self):
        print("1) Print all students\n"
            "2) Create Student\n"
            "3) Update Student\n"
            "4) Delete Student\n"
            "5) Search Student\n")



# cursor.execute("CREATE TABLE TEST ( id INT ) ")
# cursor.execute("INSERT INTO TEST (id) VALUES ('5')")
# cursor.execute("SELECT id FROM TEST ")