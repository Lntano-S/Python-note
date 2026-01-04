def main() -> int:
    
    S: float = 0
    n: int = 0
    k: int = int(input())
    while S <= k:
        n += 1
        S += 1 / n
        
    print(n)
    
if __name__ == "__main__":
    main()
# end main