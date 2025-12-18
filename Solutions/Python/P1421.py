def main() -> None:
    a, b = map(int, input().split())
    total: int = 10 * a + b
    n: int = total // 19
    print(n)
    
    
if __name__ == "__main__":
    main()
# end main