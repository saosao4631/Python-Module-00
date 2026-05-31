def ft_count_harvest_recursive():
    total = int(input("Days until harvest: "))

    def count_up(days):
        if days > total:
            print("Harvest time!")
            return
        print(f"Day {days}")
        count_up(days + 1)

    count_up(1)
	