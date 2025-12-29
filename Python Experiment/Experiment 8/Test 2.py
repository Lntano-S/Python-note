class Employee:
    def __init__(self, name: str, employee_id: int, base_salary: float):
        self.name: str = name
        self.employee_id: int = employee_id
        self.base_salary: float = base_salary
        
    def calculate_salary(self) -> float:
        return self.base_salary * 0.95
    
    def display_info(self) -> None:
        return f"===={self.name}员工基本信息====\n姓名: {self.name}\n员工ID: {self.employee_id}\n工资: {self.calculate_salary()}"
    
class FullTimeEmployee(Employee):
    bonus: float = 0
    def __init__(self, name: str, employee_id: int, base_salary: float) -> None:
        super().__init__(name, employee_id, base_salary)
        
    def calculate_salary(self) -> float:
        return self.calculate_salary() + self.bonus
    

     
        