def main() -> None:
    N: int = int(input())
    
    k: int = 1
    total: int = 0
    while total + k < N:
        total += k
        k += 1
    position: int = N - total
    
    if k % 2 == 0:
        numerator: int = position
        denominator: int = k - position + 1
    else:
        numerator: int = k - position + 1
        denominator: int = position
    
    print(f"{numerator}/{denominator}")
    
    
if __name__ == "__main__":
    main()
# end main