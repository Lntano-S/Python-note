class Student:
    def __init__(self,  
                 _name: str, 
                 _student_id: int, 
                 _age: int, 
                 _scores: dict[str, float]) -> None:
        
        self.name: str = _name
        self.student_id: int = _student_id
        self.age: int = _age
        self.scores: dict[str, float] = _scores
        
    def add_score(self, subject: str, score: float) -> None:
        self.scores[subject] = score
    
    def get_average(self) -> float:
        total: float = 0
        for v in self.scores.values():
            total += v
        
        return total / len(self.scores)
    
    def get_info(self) -> None:
        print(f"---您好！---{self.name}----")
        print(f"学号：{self.student_id}")
    
    def get_all_scores(self) -> None:
        print("成绩单:")
        for k, v in self.scores.items():
            print(f"{k}:{v}")
            
    @classmethod
    def empty_construct(cls) -> "Student":
        return Student("",0, 0, {})
    
    def __str__(self) -> str:
        return self.name
    
    
class StudentManager:
    def __init__(self) -> None:
        self.students: list[Student] = []
        
    def add_student(self, _student: Student) -> None:
        self.students.append(_student)
        
    def find_student(self, student_id: int) -> Student:
        for student in self.students:
            if student.student_id == student_id:
                return student
        return Student.empty_construct()
    
    def get_class_average(self) -> float:
        avg_scores: list[float] = []
        for student in self.students:
            avg_scores.append(student.get_average())
        return sum(avg_scores) / len(avg_scores)
    
    def show_all_students(self) -> None:
        for student in self.students:
            student.get_info()
            student.get_all_scores()

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
    print(f"学号{id1}对应的同学是{sm.find_student(id1)}")
    
    print(f"班级平均分：{sm.get_class_average():.2f}")
    
    sm.show_all_students()
    
if __name__ == "__main__":
    main()
# end main
    
    