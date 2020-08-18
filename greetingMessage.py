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

def pushGreetingMsgTemplate(to):
    line_bot_api.push_message(to, FlexSendMessage(alt_text ="Flex Message",
    contents= {
        "type": "carousel",
        "contents": [
        {
           "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://www.img.in.th/images/3878dadd9ebe81af31268a3f78ca9351.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "backgroundColor": "#FFFFFF"
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "Welcome to EDO System Assistant",
          "flex": 0,
          "size": "lg",
          "align": "center",
          "gravity": "center",
          "weight": "bold",
          "color": "#012064",
        },
        {
          "type": "text",
          "text": "Please, Login EDO System ",
          "align": "center"
        },
        {
          "type": "text",
          "text": "for use EDO System Assistant ",
          "align": "center"
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "Login",
            "uri": "https://liff.line.me/1654647285-9B24GeBR"
          },
          "color": "#0D90D4",
          "height": "sm",
          "style": "primary"
        },
        {
          "type": "spacer",
          "size": "sm"
        }
      ]
    }
        }
        ]
    }))