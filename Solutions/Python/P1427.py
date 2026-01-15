def main() -> None:
    stack: list[int] = [int(x) for x in input().split()]
    stack.pop()
    
    for _ in range(len(stack)):
        print(stack.pop(), end = " ")
        
if __name__ == "__main__":
    main()
# end main