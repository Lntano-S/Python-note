#Python 和 C++ 都是 OOP(Object Oriented Programming) 语言，即面对对象编程语言
#所以类和对象可以说是其最核心的东西了

#首先什么是对象，这个不是谈的对象，而是泛指的一类有相同属性的物品，比如一个人，都有自己的五脏六腑
#比如一个学生，都有自己的名字，年龄，学号，性别，好朋友，当处理这样相同属性的东西时
#如果我们把所有人的每个属性都单独拎出来，那样数据量和变量是会变的相当夸张的
#所以我们想了一个办法，将这群有相同特征的东西整合到一个变量身上，那就是类

#我们来看一下类的定义
class Student:
    #这里定义了一个类，类名为 Student
    #OK 我们现在有了类的名字，下一步呢，下一步就是确定这个具有共同属性的对象包含哪些属性对吧
    #这里我们会用到一个特殊函数叫做构造函数，字面意思来讲就是构造这个类的函数
    #我们通过构造函数来初始化一个类
    def __init__(self, _name: str, _age: int, _id: int, _sex: str, _friends: list["Student"] | None = None) -> None:
        #在类里面的函数传参都会带上一个self，这是为什么呢？
        #因为我们在类里面通常是对类本身的属性进行操作，调用的self其实就表示类本身
        #跟在self后面的就是我们构造这个对象的时候传进来的参数，这时候还不是对象的参数，只是我们输入进来的
        #我们一般在我们输入进来的参数前面加上一个_表示输入进来的数据
        if _friends is None:
            _friends = []
        self.name: str = _name
        self.age: int = _age
        self.id: int = _id
        self.sex: str = _sex
        #在类定义内部引用类本身作为类型时，需要使用字符串 "Student"
        self.friends: list["Student"] = _friends
        #上面的代码才真正的初始化好了对象的属性相当于定义了五个变量，都是我这个对象所具有的属性
        #然后将传进来的参数依次赋值给新定义的变量
        
    #然后我们尝试定义一个在类里面的函数用来显示自己的学号
    
    def show_id(self) -> None:
        print(f"{self.name}同学你好！你的学号是：{self.id}")
        #想要访问对象的数据就必须用self.变量名
        
    #类的便捷之处就在于我们可以随时给一个类添加新的功能
    #比如我现在想知道我有多少个朋友
    #我就可以
    
    def num_of_friends(self) -> int:
        return len(self.friends)
    
    #只需要写一次代码，就能运用到所有的对象上
    
    #这个是Python的特色，叫装饰器
    #这里的这个是一个@property装饰器
    #下面展示的是一个getter 通过函数获取对象里的数据
    @property
    def set_age(self) -> int:
        return self.age
    #在使用@property装饰器之后，这个函数就变成了一个属性了，不需要再加括号，可以直接当作变量使用
    #下面是一个 setter ，能做到给其赋值
    @set_age.setter
    def set_age(self, value: int) -> None:
        self.age = value
        
    #Python里还有一个高级玩意叫做 Magic Method
    #他可以实现很多你不敢想的功能（如果你会cpp）
    #比如
    def __str__(self) -> str:
        return f"姓名:{self.name}\n学号:{self.id}\n年龄:{self.age}\n性别:{self.sex}"
    #这个 __str__ 函数意思是，再将对象当作字符串用的时候，返回下列字符串，比如print(student1)
    #再比如
    def __add__(self, other: "Student") -> str:
        return f"哈哈哈！{self.name}和{other.name}在一起啦！！"
    #这个函数定义了给两个对象做加法
    #原谅我开这个玩笑，我想不到别的方便理解的例子了
    
#然后看看我之前自己写的一个类 是银行账户的类
class BankAccount:
    def __init__(self, id : int, name : str, money : float, account_type : str):
        self.id = id
        self.name = name
        self.money = money
        self.account_type = account_type
        
    def deposit(self, save_m : float) -> None:
        self.money += save_m
        print(f"成功存款{save_m}元，账户余额为{self.money}元")
    
    def withdraw(self, take_m : float) -> bool:
        if self.money < take_m:
            print("账户余额不足，请输入其他金额！！")
            return False
        else:
            self.money -= take_m
            print(f"成功取走{take_m}元，账户余额为{self.money}元")
            return True
    
    def get_balance(self) -> None:
        print(f"账户余额为{self.money}元")
    
    def show_info(self) -> None:
        print(f"---您好{self.name}---")
        print(f"您的账户号为：{self.id}")
        print(f"账户类型为：{self.account_type}")
        print(f"余额为：{self.money}")
        
    def cal_interest(self) -> None:
        if self.account_type == "savings account":
            print(f"您账户余额为：{self.money}元")
            print(f"一年后的余额为：{self.money * 1.03}")    
            print(f"两年后的余额为：{self.money * (1.03 ** 2)}")
            print(f"三年后的余额为：{self.money * (1.03 ** 3)}") 
        elif self.account_type == "checking account":
            print(f"您账户余额为：{self.money}元")
            print(f"一年后的余额为：{self.money * 1.01}")    
            print(f"两年后的余额为：{self.money * (1.01 ** 2)}")
            print(f"三年后的余额为：{self.money * (1.01 ** 3)}")
            
    
def main() -> None:
    #然后我们调用一下这个类
    student1: Student = Student("姚奕枫", 18, 202521095054, "male")
    #你会发现我好像漏填了一个参数
    #但为什么编译器没有报错呢
    #这是因为我在写构造函数的时候给 friends这个元素初始化为了一个空列表
    student1.show_id()
    #我们再定义一个对象
    student2: Student = Student("舒天宇", 19, 202521095025, "male")
    
    #然后姚奕枫和舒天宇交了朋友
    #我们只需要
    
    student1.friends.append(student2)
    student2.friends.append(student1)
    #这样就行了
    
    numfyyf: int = student1.num_of_friends()
    
    print (f"{student1.name}有{numfyyf}个朋友，是{student1.friends[0].name}")
    
    student1.set_age = 19
    
    print (student1)
    
    print (student1 + student2)
    
    #然后我们也可以通过数据结构来初始化类
    #比如用列表
    names: list[str] = ["刘宇杰", "丁昊哲", "田昌旭", "姚均卓"]
    students: list[Student] = [Student(names[i], 18, 2025000 + i, "male") 
                               for i in range(0, len(names))]
    for s in students:
        print (s)
    
if __name__ == "__main__":
    main()