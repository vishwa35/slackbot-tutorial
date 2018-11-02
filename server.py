from flask import Flask, request, make_response, Response
import json
from tokens import SLACK_BOT_TOKEN, SLACK_VERIFICATION_TOKEN
from slackclient import SlackClient
from slashCommand import *



slack_client = SlackClient(SLACK_BOT_TOKEN)
app = Flask(__name__)

commander = Slash("Hey there! It works.")

#TODO: Add checks for all responses from slack api calls

def verify_slack_token(request_token):
    if SLACK_VERIFICATION_TOKEN != request_token:
        print("Error: invalid verification token!")
        print("Received {} but was expecting {}".format(request_token, SLACK_VERIFICATION_TOKEN))
        return make_response("Request contains invalid Slack verification token", 403)

@app.route("/slack/mycommand", methods=["POST"])
def command():
  info = request.form

  # get uid of the user
  im_id = slack_client.api_call(
    "im.open",
    user=info["user_id"]
  )["channel"]["id"]

  # send user a response via DM
  ownerMsg = slack_client.api_call(
    "chat.postMessage",
    channel=im_id,
    text=commander.getMessage()

  # send channel a response
  channelMsg = slack_client.api_call(
    "chat.postMessage",
    channel="#" + info["channel_name"],
    text=commander.getMessage()

  return make_response("", 200)

# Start the Flask server
if __name__ == "__main__":
  app.run()