from apscheduler.schedulers.blocking import BlockingScheduler
from main import sending


sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(sending, 'interval', minutes=2)

sched.start()