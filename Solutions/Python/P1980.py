def main() -> int:
    n, x = map(int, input().split())
    total: int = 0
    base: str = str(x)
    for i in range(1, n + 1):
        sample = str(i)
        for string in sample:
            if string == base:
                total += 1
        
    print(total)
    
if __name__ == "__main__":
    main()
# end main