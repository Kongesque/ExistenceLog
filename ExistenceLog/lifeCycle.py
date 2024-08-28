def life(years):
    days_per_year = 365  
    total_days = years * days_per_year
    
    for day in range(total_days):
        print("Awoke")
        print("Slept")
    
    print("Died")

life(80)
