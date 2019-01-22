class Worker:
    """This class represents"""
    def __init__(self,worker_name=""):
        self.name = worker_name

    def set_name (self, new_name):
        self.__name = new_name

    def get_name (self, new_name):
        return self.__name

class Employee(Worker):
    """This class specializes Worker and is salarized"""
    def __init__(selfself,initial_salary):
        self.__salary = initial_salary

    def self.salary(self, new_salar)