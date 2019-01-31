import datetime

class Worker:

    def __init__(self, id: int, first_name: str,last_name: str, hire_date: datetime):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hire_date = hire_date

    def set_first_name(self, first_name: str)
        self.__first_name = first_name

    def set_last_name(self, last_name: str)
            self.__last_name = last_name

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_hire_date(self):
        return self.__hire_date


class Employee(Worker):

    def __init__(self, id: int, first_name: str, last_name: str, hire_date: datetime, salary: float):
        self.__salary = salary
        super().__init__(id,first_name,last_name,hire_date)

    def set_salary(self, salary: float):
        self.__salary = salary

    def get_salary(self,):
        return self.__salary

class Contractor(Worker):

    def __init__(self, id: int, first_name: str, last_name: str, hire_date: datetime, hourly_rate: float):
        self.__hourly_rate = hourly_rate
        super().__init__(id,first_name,last_name,hire_date)

    def set_hourly_rate(self, hourly_rate: float):
        self.__hourly_rate = hourly_rate

    def get_hourly_rate(self):
        return self.__hourly_rate

class Task:

    def __init__(self, task_id, name, description, assigned_to: Worker, duration_hours: float, work_hours_worked):
        self.__task_id = task_id
        self.__name = name
        self.__description = description
        self.__assigned_to = assigned_to
        self.__duration_hours = duration_hours
        self.__work_hours_worked = work_hours_worked

    def set_name(self,name: str):
        self.__name  = name

    def set_description(self,description):
        self.__description = description

    def set_duration_hours(self,duration_hours: float):
        self.__duration_hours = duration_hours

    def set_assigned_to(self, assigned_to: Worker):
            self.__assigned_to: assigned_to

    def set_duration_hours(self):

    def get_id(self):
        return self.__task_id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_duration_hours(self):
        return self.__duration_hours

    def get_assigned_to(self):
        return self.__assigned_to


class Project:
    def __init__(self, id: int, name: str,description: str , hours_estimated: float):
        self.__id= id
        self.__name = name
        self.__description = description

        self.__hours_estimated = hours_estimated

    def set_name(self,name: str):
        self.__name = name

    def set_hours_estimated(self,hours_estimated: float):
        self.__hours_estimated = hours_estimated


    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description


