import schedule
import time
from services import lunchService

schedule.every().day.at("01:00").do(lunchService.execute)

while True:
    schedule.run_pending()
    time.sleep(1)