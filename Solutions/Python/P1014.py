def main() -> float:
    '''
    N: int = int(input()) 
    Cantor: list[list] = [[0]] * 10**4
    a_n: int = 0
    
    for i in range(len(Cantor)):
        for j in range(len(Cantor)):
            Cantor[i][j] = i / j
            
    for k in range(1, 10**4):
        a_n += 1
        S += k
        if a_n // 2 == 0:
            if N == S:
                result = Cantor[a_n][1]
                
        else:
            if N == S:
                result = Cantor[1][a_n]
    '''            
    N: int = int(input())
    k: int = 1
    total: int = 0
    
    while total + k < N:
        position: int = total - N
        k += 1
        total += k
        
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