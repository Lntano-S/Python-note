import pandas as pd

def input_data(filepath: str) -> dict:
    df = pd.read_excel(filepath)
    
    employee_data: dict = {}
    headers = df.columns.tolist()
    for row in df.itertuples():
        # name: str = str(row[0])
        '''
            employee_data[name] = {
                headers[1]: row[1],
                headers[2]: row[2],
                headers[3]: row[3]
        }
        '''
        
        name: str = str(row.员工姓名)
        employee_data[name] = {
            "基本工资": row.基本工资,
            "奖金": row.奖金,
            "扣款": row.扣款
        }
    return employee_data    
    # print(employee_data)
    
def process_data(employee_data: dict) -> dict:
    for name, salary in employee_data.items():
        salary["实发工资"] = (salary["基本工资"] + salary["奖金"] - salary["扣款"])
    return employee_data

def output_data(employee_data: dict) -> None:
    rank: list[str] = sorted(list(employee_data.keys()), key = lambda x: employee_data[x]["实发工资"], reverse=True)
    
    print("=======个人工资条=======")
    for name, salary in employee_data.items():
        print(f"员工姓名；{name}")
        for details, wage in salary.items():
            print(f"{details}:{wage}")
        print("--------------")
            
    print("========工资排名========")        
    for i in range(len(rank)):
        print(f"第{i + 1}名：{rank[i]}")
        
    
    
if __name__ == "__main__":
    filepath: str = r"Python Experiment\Experiment 7\Test 2\员工工资.xlsx"
    
    output_data(process_data(input_data(filepath)))
# end main

