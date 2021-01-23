class employee:   #class classname
    num_employee = 0     #
    raise_amount = 1.04  #

    def __init__(self, first, last, sal):
        self.first = first
        self.last = last
        self.sal = sal
        self.email = first + '.' + last + '@company.com'
        employee.num_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.sal = int(self.sal * employee.raise_amount)


class developer(employee):
    pass

emp1 = employee("Mohammed", "Ameer", 10000)

print(emp1.sal)
