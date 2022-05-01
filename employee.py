class Employee:
    def __init__(self, name, id, title, hire_date):
        self.name = name
        self.id = id
        self.title = title
        self.hire_date = hire_date

    def create(self):
        employee = {
            "name" : self.name,
            "id" : self.id,
            "title" : self.title,
            "hire_date" : self.hire_date
        }
        return employee
