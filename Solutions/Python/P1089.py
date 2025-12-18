def main() -> None:
    budgets: list[int] = [int(input()) for _ in range(12)]
    allowance: int = 0
    saving: int = 0
    for i in range(12):
        allowance += 300
        left: int = allowance - budgets[i]
        if left >= 0:
            if left // 100 == 0:
                allowance = left
            else:
                allowance = left % 100
                saving += (left // 100) * 100
        else:
            print(-(i + 1))
            return
            
    print(int(saving * 1.2) + allowance)
    
    
if __name__ == "__main__":
    main()
# end main