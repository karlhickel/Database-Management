import sqlite3
con = sqlite3.connect("StudentDataBase.db")
cursor = con.cursor()
print("Connected to Everything.")
from MainMenu import Menu
from StudentFunctions import Student

cursor.execute("CREATE TABLE IF NOT EXISTS Student ("
               "StudentID INTEGER PRIMARY KEY AUTOINCREMENT,"
               "FirstName VARCHAR(25) NOT NULL,"
               "LastName VARCHAR(25) NOT NULL,"
               "GPA REAL,"
               "Major VARCHAR(10),"
               "FacultyAdviser VARCHAR(10)"
               ");");

#This was used to insert data into the database
#cursor.execute("INSERT INTO Student (FirstName, LastName, GPA, Major, FacultyAdviser)"
#              "VALUES ('Karl', 'Hickel', 10.0, 'Data Analytics', 'Karl Hickel')")
#cursor.execute("INSERT INTO Student (FirstName, LastName, GPA, Major, FacultyAdviser)"
#               "VALUES ('Man', 'Bone', 3.0, 'Parental Studies', 'Mike Hawk')")
#cursor.execute("INSERT INTO Student (FirstName, LastName, GPA, Major, FacultyAdviser)"
#               "VALUES ('John', 'Tone', 4.0, 'Computer Science', 'Man Bun')")
#cursor.execute("INSERT INTO Student (FirstName, LastName, GPA, Major, FacultyAdviser)"
#               "VALUES ('Karl', 'Hickel', 10.0, 'Data Analytics', 'Karl Hickel')")
#cursor.execute("INSERT INTO Student (FirstName, LastName, GPA, Major, FacultyAdviser)"
#              "VALUES ('Karl', 'Hickel', 10.0, 'Data Analytics', 'Karl Hickel')")





while True:
    StudentDatabase = Student()
    MainMenu = Menu()
    MainMenu.Menu(),
    userInput = int(input("Please Select an option"))
#Option 1
    if userInput == 1:
        StudentDatabase.displayAllStudents()

#Option 2
    elif userInput == 2:
        StudentDatabase.createStudent()

#Option 3
    elif userInput == 3:
        StudentDatabase.updateStudent()

#Option 4
    elif userInput == 4:
        StudentDatabase.deleteStudent()

#Option 5
    elif userInput == 5:
        StudentDatabase.searchStudent()


    else:
        print("Please type a valid input.")