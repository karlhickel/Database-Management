import sqlite3
con = sqlite3.connect("StudentDataBase.db")
cursor = con.cursor()

#Displays all students
class Student:
    def displayAllStudents(self):
        cursor.execute("SELECT * FROM Student")
        data = cursor.fetchall()
        con.commit()
        print(data)

#Creates a student

    def createStudent(self):
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

#Updates a student by their id number and changes their major or adviser
    def updateStudent(self):
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

#Deletes student by ID number. Checks if student exists
    def deleteStudent(self):
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

#Searches students by type of major
    def searchStudent(self):
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
                    try:
                        print("What is the students GPA?")
                        choice2 = int(input())
                        cursor.execute("SELECT * FROM Student WHERE GPA = ?", (choice2,))
                        data = cursor.fetchall()
                        con.commit()
                        print(data)




                    except Exception:
                        print("Oops you cant put words in. Please try again.")





            else:
                print("incorrect input, please try again.")
                break