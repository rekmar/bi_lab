class Group (object):
    def __init__(self, number, year):
        self.number = number
        self.year = year
        self.students = []

    @property
    def get_count_of_students(self):
        return len(self.students)

    def print_students(self):
        for st in self.students:
            print(st)

    def add_student(self, name, surname, birthdate):
        self.students.append({'name': name,
                              'surname': surname,
                              'birthdate': birthdate})

    def print_count_of_stud(self):
        print("\nCount of students in group {0} is {1}\n".
              format(self.number, self.get_count_of_students))


Group1 = Group(551002, 2015)
Group1.add_student('Maryia', 'Rekhva', '06-01-1998')
Group1.add_student('Stepan', 'Shamashow', '21-01-1998')
Group1.add_student('Nikita', 'Senko', '16-11-1997')
Group1.print_students()
Group1.print_count_of_stud()

Group2 = Group(551003, 2015)
Group2.add_student('Alina', 'Ivchenko', '06-11-1997')
Group2.print_students()
Group2.print_count_of_stud()
