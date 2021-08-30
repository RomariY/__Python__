import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack import WebClient
from slack.errors import SlackApiError

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

try:
  response = client.chat_postMessage(
    channel="C02B1LRCYH2",
    text="New ticket"
  )
except SlackApiError as e:
  assert e.response["error"]