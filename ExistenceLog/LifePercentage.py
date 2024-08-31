from datetime import datetime

def life():
    days = (datetime.now() - datetime(2003, 4, 25)).days
    
    # Average lifespan of 77.92 years is based on the user's local data.
    percentLived = (days / (77.92 * 365.25)) * 100
    
    print(f"Day {days}")
    print(f"Percentage of life lived: {percentLived:.2f}%")

life()
