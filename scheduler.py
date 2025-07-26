from apscheduler.schedulers.blocking import BlockingScheduler
import os

def run_scrapers():
    os.system("python hashtag_tracker.py")
    os.system("python audio_tracker.py")
    os.system("python email_alert.py")
    os.system("python sheets_sync.py")

scheduler = BlockingScheduler()
scheduler.add_job(run_scrapers, 'cron', hour=8)
scheduler.start()