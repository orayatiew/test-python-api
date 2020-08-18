from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
import requests 
import sys
import os
from flask import Flask, flash, request, redirect, url_for
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

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)
#CORS(app)


# @app.route('/LinkRichMenuToUser', methods=['GET'])
# def LinkRichMenuToUser(userId):
#     print('userId',str(userId))
#     rich_menu_id = 'richmenu-b607ce567e3fb7c23075e0a368a03e3c'
#     line_bot_api.link_rich_menu_to_user(userId, rich_menu_id)
#     return str(userId)

#api.add_resource(LinkRichMenuToUser, '/linkrichmenu/<userId>') # Route_1
@app.route("/api/linkrichmenu/<userId>")
@cross_origin(origin='*')
def LinkRichMenuToUser(userId):
    print('userId',str(userId))
    rich_menu_id = 'richmenu-b607ce567e3fb7c23075e0a368a03e3c'
    line_bot_api.link_rich_menu_to_user(userId, rich_menu_id)
    return {'status':'upLoadImagevFor Training'}


if __name__ == '__main__':
    app.run(port=5002)
    