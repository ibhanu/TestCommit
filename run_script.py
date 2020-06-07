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
from pushsafer import init, Client

init("O96xi4uzfIGkzMG3oeDb")

def script():
    print("Scipt commit started")
    os.system("sh commit.sh")


def run_shell():
    try:
        print("Task Started")
        logger.debug("Commit Started")
        script()
        Client("").send_message("Message", "Hello", "25630", "1", "4", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "60", "600", "1", "", "", "")

        logger.debug("Commit ended")
    except:
        logger.exception("Exception Occurred")


schedule.every().day.at("19:19").do(run_shell)

while True:
    schedule.run_pending()
    time.sleep(3)
