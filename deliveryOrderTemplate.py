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

def pushDeliveryOrderTemplate(to):
    line_bot_api.push_message(to, FlexSendMessage(alt_text ="Flex Message",
    contents= {
        "type": "carousel",
        "contents": [
        {
            "type": "bubble",
        "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "contents": [
            {
            "type": "text",
            "text": "DO20030012345",
            "flex": 0,
            "size": "xl",
            "align": "center",
            "gravity": "center",
            "weight": "bold",
            "color": "#000642"
            },
            {
            "type": "box",
            "layout": "vertical",
            "spacing": "xs",
            "margin": "md",
            "contents": [
                {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                    "type": "text",
                    "text": "S/O No. ",
                    "weight": "bold",
                    "color": "#273D8D"
                    },
                    {
                    "type": "text",
                    "text": "SO200300123",
                    "size": "sm",
                    "align": "end",
                    "weight": "bold",
                    "color": "#757575"
                    }
                ]
                },
                {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                    "type": "text",
                    "text": "P/O No.",
                    "weight": "bold",
                    "color": "#273D8D"
                    },
                    {
                    "type": "text",
                    "text": "PO100200456",
                    "size": "sm",
                    "align": "end",
                    "weight": "bold",
                    "color": "#757575"
                    }
                ]
                },
                {
                "type": "separator",
                "margin": "md",
                "color": "#11348B"
                },
                {
                "type": "box",
                "layout": "baseline",
                "margin": "sm",
                "contents": [
                    {
                    "type": "text",
                    "text": "Driver",
                    "flex": 0,
                    "margin": "sm",
                    "gravity": "top",
                    "weight": "bold"
                    },
                    {
                    "type": "text",
                    "text": "Jonh Smitt",
                    "size": "sm",
                    "align": "end",
                    "weight": "regular",
                    "color": "#AAAAAA"
                    }
                ]
                },
                {
                "type": "text",
                "text": "Taweetruck co ltd",
                "size": "xs",
                "align": "end",
                "gravity": "center",
                "weight": "regular",
                "color": "#A4A1A1"
                },
                {
                "type": "box",
                "layout": "baseline",
                "margin": "sm",
                "contents": [
                    {
                    "type": "text",
                    "text": "Car Type",
                    "margin": "xs",
                    "size": "md",
                    "weight": "bold"
                    },
                    {
                    "type": "text",
                    "text": "Truck 10 Wheels",
                    "size": "xs",
                    "align": "end",
                    "weight": "bold",
                    "color": "#A1A2A4"
                    }
                ]
                },
                {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                    "type": "text",
                    "text": "license plate",
                    "margin": "sm",
                    "size": "sm",
                    "gravity": "top",
                    "weight": "bold"
                    },
                    {
                    "type": "text",
                    "text": "AB-23456",
                    "size": "md",
                    "align": "end",
                    "weight": "bold",
                    "color": "#B3B3B3"
                    }
                ]
                },
                {
                "type": "box",
                "layout": "baseline",
                "spacing": "xl",
                "margin": "xs",
                "contents": [
                    {
                    "type": "text",
                    "text": "Container No. ",
                    "margin": "sm",
                    "size": "sm",
                    "gravity": "top",
                    "weight": "bold"
                    },
                    {
                    "type": "text",
                    "text": "TM-54G-345",
                    "size": "sm",
                    "align": "end",
                    "weight": "bold",
                    "color": "#B3B3B3"
                    }
                ]
                },
                {
                "type": "separator",
                "margin": "xs",
                "color": "#0F54A1"
                }
            ]
            },
            {
            "type": "box",
            "layout": "vertical",
            "spacing": "xs",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                    "type": "text",
                    "text": "Mono Ethylene (MEG)",
                    "size": "sm",
                    "weight": "bold"
                    },
                    {
                    "type": "text",
                    "text": "(EGTM.M000014)",
                    "size": "xs"
                    }
                ]
                },
                {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                    "type": "text",
                    "text": "Amount",
                    "size": "xs",
                    "weight": "bold"
                    },
                    {
                    "type": "text",
                    "text": "20,000 KG/ 20 Bag",
                    "size": "xs",
                    "align": "end",
                    "weight": "bold"
                    }
                ]
                },
                {
                "type": "separator",
                "margin": "xs"
                }
            ]
            },
            {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                    "type": "text",
                    "text": "Mono Ethylene (MEG)",
                    "size": "sm",
                    "weight": "bold"
                    },
                    {
                    "type": "text",
                    "text": "(EGTM.M000014)",
                    "size": "xs"
                    }
                ]
                },
                {
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                    "type": "text",
                    "text": "Amount",
                    "size": "xs",
                    "weight": "bold"
                    },
                    {
                    "type": "text",
                    "text": "20,000 KG/ 20 Bag",
                    "size": "xs",
                    "align": "end",
                    "weight": "bold"
                    }
                ]
                },
                {
                "type": "separator"
                }
            ]
            }
        ]
        },
        "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "xs",
        "margin": "xs",
        "contents": [
            {
            "type": "spacer",
            "size": "sm"
            },
            {
            "type": "button",
            "action": {
                "type": "uri",
                "label": "Complated",
                "uri": "https://liff.line.me/1654647285-oaAWXkR3?q=123456"
            },
            "color": "#1DB95B",
            "height": "sm",
            "style": "primary",
            "gravity": "center"
            },
            {
            "type": "button",
            "action": {
                "type": "uri",
                "label": "Partial Received",
                "uri": "https://liff.line.me/1654647285-oaAWXkR3?q=123456"
            },
            "color": "#2B68C6",
            "margin": "sm",
            "height": "sm",
            "style": "primary"
            }
        ]
        }
        }
        ]
    }))