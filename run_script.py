import os
import logging
import time
import schedule


logging.basicConfig(filename="script.log",
                    format='%(asctime)s %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("Logger Started")


def script():
    os.system("sh commit.sh")


def run_shell():
    try:
        logger.debug("Commit Started")
        script()
        logger.debug("Commit ended")
    except:
        logger.exception("Exception Occurred")


schedule.every().day.at("00:40").do(run_shell)

while True:
    schedule.run_pending()
    time.sleep(3)
