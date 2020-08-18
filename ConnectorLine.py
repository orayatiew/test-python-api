from flask import Flask, request, abort
import sys
import os
from deliveryOrderTemplate import *
from greetingMessage import *
from deliveryToday import *
from doParameter import *
from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    FollowEvent, MessageEvent, TextMessage, TextSendMessage,FlexSendMessage
)

app = Flask(__name__)
line_bot_api = LineBotApi('otJs5SdG/q3EB7zY0jWpPtkoUP0YIZAKeTxtIiBc3fLzwejucW06UFaH6k6sx57gg4jF/NHgiQRLfcnn5GxIAeveCZqTDfIJU5pmT/Mf4VG9Wfrz2saHxNN/+pnLDhy/Dhc/Lo4DoEKjrQE1Hvw+SAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a6eaf3123707544bf4e0927af0cea4b8')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    #app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event"+ str(event))
    print("event get user Id"+ str(event.source.user_id))
    print(event.message.text)
    if (event.message.text == "Delivering"):
        pushDeliveryOrderTemplate(event.source.user_id)
    if (event.message.text == "Delivery Today"):
        deliveryToday(event.source.user_id)
    if ("DO" in event.message.text):
        print("in")
        deliveryOrderParam(event.source.user_id,event.message.text)    

    # to = 'U7a441220a7beea59ef98a58e8b323d1a'
    # pushDeliveryOrderTemplate(to)
    #line_bot_api.push_message(to, TextSendMessage(text="https://liff.line.me/1654647285-9B24GeBR"))
    
    #line_bot_api.reply_message(
        #event.reply_token,
        #TextSendMessage(text=event.message.text))

@handler.add(FollowEvent)
def handle_follow(event):
    print("event add friend"+ str(event))
    user = event.source.user_id
    print(user)
    pushGreetingMsgTemplate(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=int(os.environ.get('PORT','5000')))