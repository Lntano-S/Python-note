class Employee:
    def __init__(self, 
                _name: str,
                _employee_id: int,
                _base_salary: int
                ) -> None:
        self.name: str =_name
        self.employee_id: int = _employee_id
        self.base_salary: int = _base_salary
    
    def calculate_salary(self) -> int:
        return self.base_salary - self.base_salary * 0.05
    
    def display_info(self) -> None:
        print(f"----您好--{self.name}----")
        print(f"您的id是{self.employee_id}")
        print(f"您的工资为{self.calculate_salary()}")
    
class FullTimeEmployee(Employee):
    def __init__(self,
                _name: str,
                _employee_id: int, 
                _base_salary: int,
                _bonus: int
                ) -> None:
        super().__init__(_name, _employee_id, _base_salary)
        self.bonus: int = _bonus
    
    def calculate_salary(self) -> int:
        return super().calculate_salary() + self.bonus

class PartTimeEmployee(Employee):
    def __init__(self, 
                _name: str, 
                _employee_id: int,
                _base_salary: int,
                _hours_worked: int,
                _hourly_rate: int
                ) -> None:
        super().__init__(_name, _employee_id, _base_salary)
        self.hours_worked: int = _hours_worked
        self.hourly_rate: int = _hourly_rate
    
    def calculate_salary(self) -> int:
        return self.hourly_rate * self.hours_worked
    
def main() -> None:
    fte = FullTimeEmployee("姚奕枫", 1, 9000, 2000)
    pte = PartTimeEmployee("舒天宇", 2, 9000, 20, 90)
    
    fte.display_info()
    pte.display_info()
    print()
    print(f"{fte.name}的工资为{fte.calculate_salary()}")
    print(f"{pte.name}的工资为{pte.calculate_salary()}")
    
    
if __name__ == "__main__":
    main()
# end main