def ft_count_harvest_recursive():
    total = int(input("Days until harvest: "))
    for i in range(1, total + 1, 1):
        print(f"Day {i}")
    print("Harvest time!")
