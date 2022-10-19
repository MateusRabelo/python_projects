import time

def countdown(times):
    while times:
        
        mins, secs = divmod(times, 60)
        timer = "{:02d}:{:02d}". format(mins, secs)
        
        print(timer, end='\r')
        time.sleep(1)
        times -= 1
    print("timer completed!")
    
    
times = input("Enter the time in seconds: ")
countdown(int(times))
        