def ft_waterr_reminder():
    days = int(input("Days since last watering: "))
    if days > 1:
        print("Water the plants!")
    else:
        print("Plants are fine")
