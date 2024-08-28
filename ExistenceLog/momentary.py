import time

def life():
    moments = 0
    while True:
        moments += 1
        print(f"Moment: {moments}")
        time.sleep(1) 

life()
