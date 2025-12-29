class Student:
    def __init__(self, name: str, student_id: int, age: int, scores: dict) -> None:
        self.name: str = name 
        self.student_id: int = student_id
        self.age: int = age
        self.scores: dict = scores
    
    # 实例方法： 添加或更新一门科目的成绩
    def add_score(self, subject: str, score: float) -> dict:
        self.scores[subject] = score
        return self.scores
    
    # 实例方法： 所有科目的平均分
    def get_average(self) -> float:
        total = 0
        for score in self.scores.values():
            total += score
        return total / len(self.scores)
    
    # 实例方法： 返回学生的基本信息
    def get_info(self) -> str:
            return f"=====学生基本信息=====\n姓名: {self.name}\n学号:{self.student_id}\n年龄: {self.age}"
        
    # 实例方法： 返回所有科目成绩
    def get_all_scores(self) -> str:
        result = f"----{self.name}的所有科目成绩----\n"
        for subject, score in self.scores.items():
            result += f"{subject}: {score}\n"
        return result
    
    @classmethod
    def empty_ob(cls):
        return Student("", 0, 0, {})
    
class StudentManager:
    def __init__(self) -> None:
        self.students: list[Student] = []

    # 实例方法： 添加学生到管理系统        
    def add_student(self, student: Student) :
        self.students.append(student)

    # 实例方法： 根据学号查找学生
    def find_student(self, student_id: int):
        for student in self.students:
            if student.student_id == student_id:
                return student.name
        return Student.empty_ob()
        
    # 实例方法： 班级所有学生的平均分
    def get_class_average(self) -> float:
        avg_scores: list = []
        for student in self.students:
            avg_scores.append(student.get_average())
        return sum(avg_scores) / len(avg_scores)
    
    # 实例方法： 所有学生信息及成绩
    def show_all_students(self) -> None:
        for student in self.students:
            print(student.get_info())
            print(student.get_all_scores())
            
def main() -> None:
    student1 = Student("姚奕枫", 202521095054, 18, {})
    student2 = Student("舒天宇", 202521095025, 19, {})
    student3 = Student("张晋铭", 202521095060, 19, {})
    
    
    student1.add_score("语文", 74.0)
    student1.add_score("数学", 121.0)
    student1.add_score("英语", 134.0)
    student2.add_score("语文", 112.0)
    student2.add_score("数学", 108.0)
    student2.add_score("英语", 131.0)
    student3.add_score("语文", 121.0)
    student3.add_score("数学", 109.0)
    student3.add_score("英语", 128.0)
    
    sm = StudentManager()
    
    sm.add_student(student1)
    sm.add_student(student2)
    sm.add_student(student3)
    
    id1: int = 202521095025
    print(f"学号为{id1}的学生为{sm.find_student(id1)}")
    
    print(f"班级平均分为{sm.get_class_average():.2f}")
    
    sm.show_all_students()
    
if __name__ == "__main__":
    main()