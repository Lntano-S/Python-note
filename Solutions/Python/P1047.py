def main():
    l,m = map(int, (input().split()))
    trees: list[int] = [1] * (l + 1)
    
    for _ in range(m):
        u, v = map(int, input().split()) 
        for i in range(u, v + 1):
            trees[i] = 0
            
    return sum(trees)

if __name__ == "__main__":
    print(main())
# end main
    