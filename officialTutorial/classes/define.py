
class IntSet(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    
    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    
    def getMembers(self):
        return self.vals[:]

    def __str__(self):
        self.vals.sort()
        results = ''
        for e in self.vals:
            results = results + str(e) + ','
        return '{' + results[:-1] + '}' # -1 omits the trailing comma

# s = IntSet()
# s.insert(3)
# print(s.member(3))

import datetime

class Person(object):

    def __init__(self, name: str):
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

    def setBirthday(self, birthdate):
        self.birthday = birthdate
    
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other: 'Person'): # use ' ' , otherwise there would be an error
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name
    
# me = Person('Michael Guttag')
# him = Person('Barack Hussein Obama')
# her = Person('Madonna')
# print(him.getLastName())
# him.setBirthday(datetime.date(1961, 8, 4))
# her.setBirthday(datetime.date(1958, 8, 16))
# print(him.getName(), 'is', him.getAge(), 'days old')


class TJPerson(Person):
    
    nextIdNum = 0
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = TJPerson.nextIdNum
        TJPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

class Student(TJPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        TJPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year

class Grad(Student):
    pass

## test codes
# p5 = Grad('Buzz Aldrin')
# p6 = UG('Billy Beaver', 1984)
# print(p5, 'is a graduate student is', type(p5) == Grad)
# print(p5, 'is an undergraduate student is', type(p5) == UG)

class Grades(object):
    """ The grades of a particular subject
    """
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
    
    def addStudent(self, student: Student):
        if student in self.students:
            raise ValueError('Duplicate student')
        else:
            self.students.append(student)
            self.grades[student.getIdNum()] = []
            self.isSorted = False
    
    def addGrade(self, student: Student, grade: float):
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('unknown student')

    def getGrades(self, student: Student):
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('unknown student')

    def getStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s



pass #  add a breakpoint her





