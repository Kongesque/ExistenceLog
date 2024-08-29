import datetime

def life():
    start_date = datetime.datetime(2003, 4, 25)
    now = datetime.datetime.now()
    days = (now - start_date).days
    
    print(f"Day {days}: You wake up again. The clock ticks. Nothing has changed. Continue? (Y/N)")

life()
