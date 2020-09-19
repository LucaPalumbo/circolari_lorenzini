from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


sched = BackgroundScheduler()

# Start the scheduler

def job_function():
    print( "Hello World")
def job2():
    print("Hello World 22")


# Schedule job_function to be called every two hours
sched.add_job(job_function,"interval", seconds=2, id="job1")

# The same as before, but start after a certain time point
sched.add_job(job2,"interval" ,seconds=5, id="job2")

sched.start()

while 1:
    pass