class StudentAttributes:
    def __init__(self, FirstName, LastName, GPA, Major, FacultyAdviser):
        self.FirstName = str(FirstName)
        self.LastName = str(LastName)
        self.GPA = float(GPA)
        self.typeMajor = str(Major)
        self.nameAdviser = str(FacultyAdviser)