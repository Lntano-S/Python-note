def main() -> None:
    busiest: int = -1
    busiest_day: int = 0
    for i in range(7):
        on_school, after_school = map(int, input().split())
        if on_school + after_school > 8 and on_school + after_school > busiest:
            busiest = on_school + after_school
            busiest_day = i + 1

    print (busiest_day)


if __name__ == "__main__":
    main()