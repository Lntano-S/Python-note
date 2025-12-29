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
        result = f"===={self.name}的所有科目成绩===="
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
                return student
            else:
                return student.empty_ob()
        return None
        
    # 实例方法： 班级所有学生的平均分
    def get_class_average(self) -> float:
        avg_scores: list = []
        for student in self.students:
            avg_scores.append(student.get_average())
        return sum(avg_scores) / len(avg_scores)
    
    # 实例方法： 所有学生信息及成绩
    def sholl_all_students(self)  -> None:
        
    
    