def main() -> None:
    n: int = int(input())
    pen1, price1 = map(int, input().split())
    pen2, price2 = map(int, input().split())
    pen3, price3 = map(int, input().split())
    
    money: list[int] = []
    pen_ls: list[int] = [pen1, pen2, pen3]
    price_ls: list[int] = [price1, price2, price3]
    
    for i in range(3):
        if n % pen_ls[i] == 0:
            money.append((n // pen_ls[i]) * price_ls[i])
        else:
            money.append((n // pen_ls[i] + 1) * price_ls[i])

    print(min(money))
    
if __name__ == "__main__":
    main()
# end main