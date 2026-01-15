def main() -> int:
    N = int(input())
    if_pos: int = 1
    if N < 0: if_pos = -1
    
    N_str = str(abs(N))
    
    if N_str[len(N_str) - 1] != 0:
        return int(N_str[::-1]) * if_pos
    else:
        return int(N_str[:len(N_str) - 1:-1]) * if_pos
        

    
if __name__ == "__main__":
    print(main())
# end main