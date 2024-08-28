import random

def life(years):
    days_per_year = 365  
    total_days = years * days_per_year
    death_chance = 0.00027347324
    
    for day in range(total_days):
        if random.random() < death_chance:
            print("Died")
            break
        else:
            print("Awoke")
            print("Slept")
    else:
        print("Died of old age")

life(80)
