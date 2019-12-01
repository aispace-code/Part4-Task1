class Student:
    def __init__ (self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def full_info(self):
        return '{} {} {} {} {} {}'.format(self.name, self.lastname, 'entered', self.department, 'in', self.year_of_entrance)

person1 = Student('Aisuluu ', 'Kydyralieva ', 'International Relations department ', ' 2016 ')

print(person1.full_info())

#формат добавить