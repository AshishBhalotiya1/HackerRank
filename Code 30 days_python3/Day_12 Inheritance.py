class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, score):
        super().__init__(firstName, lastName, idNumber)
        self.score = score

    def calculate(self):
        totalscore = 0
        for i in range(len(self.score)):
            totalscore += self.score[i]
        Average = totalscore / len(self.score)
        if Average >= 90:
            return "O"
        elif Average >= 80:
            return "E"
        elif Average >= 70:
            return "A"
        elif Average >= 55:
            return "P"
        elif Average >= 40:
            return "D"
        elif Average < 40:
            return "T"


if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input())  # not needed for Python
    scores = list(map(int, input().split()))
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
