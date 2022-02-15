def water_left(astronaunt,water_left,days_left):
    daily_usage = astronaunt * 11
    total_usage= daily_usage * days_left
    total_water_left = water_left - total_usage
    print(f"Total water left after {days_left} days is: {total_water_left} liters")
    # si tenemos poca agua o menor a 0 vamos hacer una exception
    if total_water_left<0:
       raise RuntimeError(f"There is not enough water for {astronaunt} astronaunts after {days_left} days!")

water_left(5,100,2)
