#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from flask import Flask, request, abort
import sys
import os
import sys
import os
from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FlexSendMessage
)
line_bot_api = LineBotApi('otJs5SdG/q3EB7zY0jWpPtkoUP0YIZAKeTxtIiBc3fLzwejucW06UFaH6k6sx57gg4jF/NHgiQRLfcnn5GxIAeveCZqTDfIJU5pmT/Mf4VG9Wfrz2saHxNN/+pnLDhy/Dhc/Lo4DoEKjrQE1Hvw+SAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a6eaf3123707544bf4e0927af0cea4b8')

app = Flask(__name__)
log = app.logger

def deliveryToday(to):
    line_bot_api.push_message(to, FlexSendMessage(alt_text ="Flex Message",
    contents= {
        "type": "carousel",
        "contents": [
        {
         "type": "bubble",
    "header": {
      "type": "box",
      "layout": "horizontal",
      "spacing": "xs",
      "contents": [
        {
          "type": "text",
          "text": "Delivery Order List Today",
          "margin": "none",
          "size": "sm",
          "weight": "bold",
          "color": "#1B72A8"
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "spacing": "xs",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "flex": 2,
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "margin": "md",
              "contents": [
                {
                  "type": "text",
                  "text": "DO200300001",
                  "flex": 1,
                  "size": "md",
                  "align": "start",
                  "gravity": "top",
                  "weight": "bold",
                  "color": "#000000"
                },
                {
                  "type": "text",
                  "text": "view",
                  "align": "end",
                  "weight": "bold",
                  "color": "#0E608A",
                  "action": {
                    "type": "message",
                    "label": "dono",
                    "text": "DO200300001"
                  }
                },
                {
                  "type": "spacer"
                }
              ]
            },
            {
              "type": "separator",
              "margin": "md"
            },
            {
              "type": "box",
              "layout": "baseline",
              "margin": "md",
              "contents": [
                {
                  "type": "text",
                  "text": "DO200300002",
                  "align": "start",
                  "weight": "bold",
                  "color": "#000000"
                },
                {
                  "type": "text",
                  "text": "view",
                  "align": "end",
                  "weight": "bold",
                  "color": "#0E608A",
                  "action": {
                    "type": "message",
                    "label": "dono",
                    "text": "DO200300002"
                  }
                },
                {
                  "type": "spacer"
                }
              ]
            },
            {
              "type": "separator",
              "margin": "md"
            },
            {
              "type": "box",
              "layout": "baseline",
              "margin": "md",
              "contents": [
                {
                  "type": "text",
                  "text": "DO200300003",
                  "align": "start",
                  "weight": "bold",
                  "color": "#000000"
                },
                {
                  "type": "text",
                  "text": "view",
                  "align": "end",
                  "weight": "bold",
                  "color": "#0E608A",
                  "action": {
                    "type": "message",
                    "label": "dono",
                    "text": "DO200300003"
                  }
                },
                {
                  "type": "spacer",
                  "size": "md"
                }
              ]
            }
          ]
        }
      ]
    }
        }
        ]
    }))