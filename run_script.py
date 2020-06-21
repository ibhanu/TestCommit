import os
import logging
import time
import schedule

print("Script Started")
logging.basicConfig(filename="script.log",
                    format='%(asctime)s %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("Logger Started")

def script():
    print("Scipt commit started")
    os.system("sh commit.sh")


def run_shell():
    try:
        print("Task Started")
        logger.debug("Commit Started")
        script()
        logger.debug("Commit ended")
    except:
        logger.exception("Exception Occurred")


schedule.every().day.at("19:19").do(run_shell)

while True:
    schedule.run_pending()
    time.sleep(3)
