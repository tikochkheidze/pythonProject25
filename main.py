class parent:
    def __int__(self,subjects, course, grant):
        self.subjects=subjects
        self.course=course
        self.grant=grant

    def print(self):
        print("subjects are:", self.subjects,
              " course is :", self.course,
              "grant: ", self.grant)
class student(parent):
    pass
s= student('blaablaaaa' , 'ragaca', '50%')

print("subjects are:", s.subjects , "course is: ", s.course, "grant : " , s.grant)
s.show()
