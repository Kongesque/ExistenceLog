def life(years):
    days_per_year = 365  
    total_days = years * days_per_year
    
    for day in range(total_days):
        if day % 2 == 0:
            print("Slept")
        else:
            print("Awoke")
    
    print("Died")

life(80)
