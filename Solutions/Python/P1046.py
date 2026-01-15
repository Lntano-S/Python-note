def main():
    apple_height: list[int] = [int(x) for x in input().split()]
    touch: int = int(input())
    total: int = 0
    
    for i in range(10):
        if touch + 30 >= apple_height[i]:
            total += 1
            
        else:
            total = total
            
    return total

if __name__ == "__main__":
    print(main())
# end main