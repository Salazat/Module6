class Human: #Базовым классов
    head = True
    _legs = True
    __arms = True

    # def __init__(self):
    #     self.about()
    def say_hello(self):
        print('Здравствуйте')


    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)


class Student(Human): #Дочерним классом
     pass
    # head = False

    # def about(self):
    #     print('Я студент')




class Teacher(Human):
    pass



human = Human()
human.about()

student = Student()


print(student._Human__arms)


# student = Student()
# teacher = Teacher()
# student.say_hello()
# teacher.say_hello()
# print(student.head)
