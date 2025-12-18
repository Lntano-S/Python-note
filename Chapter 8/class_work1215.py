def input_data() -> dict:
    info: dict[str, dict] = {}
    while True:
        name = str(input("请输入姓名，退出请按 0:"))
        if name == "0": break
        score: list[float] = [float(x) for x in input("请输各科分数（按照语文数学英语的顺序，并用空格隔开）：").split()]
        if name not in info:
            info[name] = dict(zip(["语文", "数学", "英语"], score))
    return info

def process_data(data: dict[str, dict]) -> dict:
    for name, scores in data.items():
        score: list[float] = [s for s in scores.values()]
        data[name]["平均分"] = sum(score) / len(score)
    return data

def output_data(data: dict[str, dict]) -> None:
    rank: list[str] = sorted([name for name in data.keys()], key=lambda x: data[x]["平均分"], reverse=True)
    print("总体成绩单：")
    for student, scores in data.items():
        print("------------------")
        print(f"{student}:")
        for sub, score in list(scores.items())[:3]:
            print(f"{sub}:{score}")
    
    print("排名：")
    for i in range(0, len(rank)):
        print(f"第{i + 1}名：{rank[i]}")

if __name__ =="__main__":
    output_data(process_data(input_data()))
    
