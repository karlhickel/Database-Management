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



