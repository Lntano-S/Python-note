def main():
    n = int(input())
    num_ls: list[int] = [int(x) for x in input().split()]
    total_set: set = set()
    count: int = 0
    
    for i in range(len(num_ls) - 1):
        for j in range(i + 1, len(num_ls)):
            total_set.add(num_ls[i] + num_ls[j])
            
    for x in num_ls:
        if x in total_set:
            count += 1
            
    print(count)
    
if __name__ == "__main__":
    main()
# end main