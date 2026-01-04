class Employee:
    def __init__(self, name: str, employee_id: int, base_salary: float):
        self.name: str = name
        self.employee_id: int = employee_id
        self.base_salary: float = base_salary
        
    def calculate_salary(self) -> float:
        return self.base_salary * 0.95
    
    def display_info(self) -> str:
        return f"===={self.name}员工基本信息====\n姓名: {self.name}\n员工ID: {self.employee_id}\n工资: {self.calculate_salary()}\n----------------"
    
class FullTimeEmployee(Employee):
    def __init__(self, 
                 name: str, 
                 employee_id: int, 
                 base_salary: float, 
                 bonus: float) -> None:
        super().__init__(name, employee_id, base_salary)
        self.bonus: float = bonus
        
    def calculate_salary(self) -> float:
        return super().calculate_salary() + self.bonus
    
class PartTimeEmployee(Employee):
    def __init__(self, name: str, 
                 employee_id: int, 
                 base_salary: float, 
                 hours_worked: float, 
                 hourly_rate: float):
        super().__init__(name, employee_id, base_salary)
        self.hours_worked: float = hours_worked
        self.hourly_rate: float = hourly_rate
        
    def calculate_salary(self) -> float:
        return self.hours_worked * self.hourly_rate
    
def main() -> None:
    employee1: FullTimeEmployee = FullTimeEmployee("舒天宇", 202521095025, 2800, 540)
    employee2: PartTimeEmployee = PartTimeEmployee("姚奕枫", 202521095054, 2800, 30, 60)
    
    print(employee1.display_info())
    
    print(f"员工{employee1.name}的薪资为{employee1.calculate_salary()}")
    print(f"员工{employee2.name}的薪资为{employee2.calculate_salary()}")
    
if __name__ == "__main__":
    main()
    
    
     
        