import os
import schedule
import time
import logging
from slackclient import SlackClient

logging.basicConfig(level=logging.DEBUG)

def sendMessage(slack_client, msg):
  # make the POST request through the python slack client
  updateMsg = slack_client.api_call(
    "chat.postMessage",
    channel='#test',
    text=msg
  )

  # check if the request was a success
  if updateMsg['ok'] is not True:
    logging.error(updateMsg)
  else:
    logging.debug(updateMsg)

if __name__ == "__main__":
  SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
  slack_client = SlackClient(SLACK_BOT_TOKEN)
  logging.debug("authorized slack client")

  # # For testing
  msg = "Good Morning!"
  schedule.every(60).seconds.do(lambda: sendMessage(slack_client, msg))

  # schedule.every().monday.at("13:15").do(lambda: sendMessage(slack_client, msg))
  logging.info("entering loop")

  while True:
    schedule.run_pending()
    time.sleep(5) # sleep for 5 seconds between checks on the scheduler
