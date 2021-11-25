from apscheduler.schedulers.blocking import BlockingScheduler
from main import sending


sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(sending, 'interval', seconds=10000)

sched.start()