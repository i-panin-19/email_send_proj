import time
from apscheduler.schedulers.background import BackgroundScheduler


def auto_job():
    seconds = time.time()
    local_time = time.ctime(seconds)
    print('Время:', local_time)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(auto_job, 'interval', seconds=30)
    scheduler.start()
