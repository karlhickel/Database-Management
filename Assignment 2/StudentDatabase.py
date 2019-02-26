import sqlite3
con = sqlite3.connect("StudentDataBase.db")
cursor = con.cursor()
print("Connected to Everything.")

# cursor.execute("CREATE TABLE TEST ( id INT ) ")
# cursor.execute("INSERT INTO TEST (id) VALUES ('5')")
# cursor.execute("SELECT id FROM TEST ")

cursor.execute("CREATE TABLE IF NOT EXISTS Student ("
               "StudentID INTEGER PRIMARY KEY AUTOINCREMENT,"
               "FirstName VARCHAR(25) NOT NULL,"
               "LastName VARCHAR(25) NOT NULL,"
               "GPA REAL,"
               "Major VARCHAR(10),"
               "FacultyAdviser VARCHAR(10)"
               ");");
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

def Menu():
    print("1) Print all students\n"
          "2) Create Student\n"
          "3) Update Student\n"
          "4) Delete Student\n"
          "5) Search Student\n")

def displayAllStudents():
    cursor.execute("SELECT * FROM Student")
    data = cursor.fetchall()
    con.commit()
    print(data)

def createStudent():
    print("Type first name")
    FirstName = raw_input()
    print("Type last name")
    LastName = raw_input()
    print("Input student GPA")
    while True:
        try:
            GPA = int(input())
            break

        except Exception:
            print("Oops you cant put words in. Please try again.")
    print("Input the major")
    typeMajor = raw_input()
    print("Input adviser")
    nameAdviser = raw_input()

    cursor.execute("INSERT INTO Student (FirstName, LastName, GPA, Major, FacultyAdviser)"
                   "VALUES (?, ?, ?, ?, ?)", (FirstName, LastName, GPA, typeMajor, nameAdviser))

    data = cursor.fetchall()
    con.commit()


def updateStudent():
    while True:
        print("Input the id of the student that you would like to update.")
        ID = int(input())
        cursor.execute("SELECT StudentID FROM Student WHERE StudentID = ?", (ID,))
        data = cursor.fetchone()
        if data is not None:
            while True:
                print("Would you like to update their major or their adviser?")
                choice = raw_input()
                if choice.upper() == 'MAJOR':
                    nameMajor = raw_input("Major name:")
                    cursor.execute("UPDATE Student SET Major = ? WHERE StudentID = ?", (nameMajor, ID))
                    data = cursor.fetchall()
                    con.commit()
                    break
                elif choice.upper() == 'ADVISER':
                    nameAdviser = raw_input("Adviser name:")
                    cursor.execute("UPDATE Student SET FacultyAdviser = ? WHERE StudentID = ?", (nameAdviser, ID))
                    data = cursor.fetchall()
                    con.commit()
                    break
                else:
                    print("Please type a valid option.")


            break
        else:
            print("Sorry ID values does not exist.")
            break


def deleteStudent():
    print("Type the ID of the student that you would like to delete.")
    while True:
        try:
            print("What is the student ID?")
            ID = int(input())
            cursor.execute("SELECT StudentID FROM Student WHERE StudentID = ?", (ID,))
            data = cursor.fetchone()
            if data is not None:
                cursor.execute("DELETE FROM Student WHERE StudentID = ?", (ID,))
                print("Student has successfully been deleted.")
                break
            else:
                print("Sorry ID values does not exist.")
                break
        except Exception:
            print("Oops you cant put words in. Please try again.")

def searchStudent():
    print("Would you like to search students by major,GPA or adviser?")
    choice = raw_input()
    while True:
        if choice.upper() == 'MAJOR':
            print("What major would you like to search by?")
            choice2 = raw_input()
            cursor.execute("SELECT * FROM Student WHERE Major = ?", (choice2,))
            data = cursor.fetchall()
            con.commit()
            print(data)
            break

        elif choice.upper() == 'ADVISER':
            print("What is the advisers name?")
            choice2 = raw_input()
            cursor.execute("SELECT * FROM Student WHERE Adviser = ?", (choice2,))
            data = cursor.fetchall()
            con.commit()
            print(data)
            break

        elif choice.upper() == 'GPA':
            while True:
                try:
                    print("What is the students GPA?")
                    choice2 = int(input())
                    cursor.execute("SELECT * FROM Student WHERE GPA = ?", (choice2,))
                    data = cursor.fetchall()
                    con.commit()
                    print(data)
                    break

                except Exception:
                    print("Oops you cant put words in. Please try again.")


        else:
            print("incorrect input, please try again.")
        break





while True:
    Menu(),
    userInput = int(input("Please Select an option"))
#Option 1
    if userInput == 1:
        displayAllStudents()

#Option 2
    elif userInput == 2:
        createStudent()

#Option 3
    elif userInput == 3:
        updateStudent()

#Option 4
    elif userInput == 4:
        deleteStudent()

#Option 5
    elif userInput == 5:
        searchStudent()


    else:
        print("Please type a valid input.")