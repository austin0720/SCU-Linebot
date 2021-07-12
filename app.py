import pyimgur
import time
import selenium
from PIL import Image
from selenium import webdriver
from flask import Flask
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageAction, ButtonsTemplate, \
    ImageCarouselTemplate, ImageCarouselColumn, URIAction,\
    CarouselTemplate, CarouselColumn, ImageMessage, FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,\
    QuickReply, QuickReplyButton, ImageSendMessage, URITemplateAction,\
    MessageTemplateAction, PostbackTemplateAction
from linebot import LineBotApi, WebhookHandler
from flask import request, abort
from linebot.exceptions import InvalidSignatureError
from linebot.models.messages import Message
from app2 import R, space1, space2, space3


app = Flask(__name__)


line_bot_api = LineBotApi(
    "RwN9U8btqMxeYXcAL4UWrhT5FAvfEZoohki4sw5WcSaJHgBJZRsRR/nLPSA+UkhTEthLpd3sxy8tC7ALbmIuwucHnAzr41vzOVjzxokvRYsknf/LX2g/ta1PlFns++6V26sYaHH1yMDwaMH8mk7NtAdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("463e2dea03c61fe2ad0cba62751e22f8")


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except IndentationError:
        abort(400)
    return 'ok'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == "我想要知道東吳人常用的網站!":
        scu_web(event)
    elif mtext == "我想要知道東吳人在校內都去哪裡!":
        scu_space(event)
    elif mtext == "我想要租借空間!":
        space(event)
    elif mtext == "人工劃記":
        space_handwrit(event)
    elif mtext == "網路登記":
        space_online(event)
    elif mtext == '我想查看【D棟學習進行室】的租借情況':
        space_online_D(event)
    elif mtext == '完成室預約情況':
        space_online_D1(event)
    elif mtext == '未來室預約情況':
        space_online_D2(event)
    elif mtext == '現在室預約情況':
        space_online_D3(event)
    elif mtext == '我想查看【R棟會議室】的租借情況':
        space_online_R(event)


def scu_web(event):
    message = TextSendMessage(
        text="1. 東吳脫殼版----所有人當你的Air Tag \n https://www.facebook.com/groups/SCUTALK/ \n2. 東吳二手書----省錢找書好地方\n https://www.facebook.com/groups/SCUBOOK/ \n3. 東吳校務行政系統 ----成績查詢、選課\n https://web.sys.scu.edu.tw/default.asp \n4. 東吳新教務系統 ----雙主修、輔系、第二專長登記處\n https://api.sys.scu.edu.tw/academic/ \n5. 東吳ALL PASS指南---- 老師給分甜不甜\n http://scupass.com/ \n6. 東吳電子化校園系統----只能用ＩＥ打開的爛東西\n http://www1.ecampus.scu.edu.tw/ \n7. SCU Moodle數位平台----上課講義都放這\n http://isee.scu.edu.tw/ \n8. 東吳Tronclass----最新數位平台\n https://tronclass.scu.edu.tw/ \n9. SCU Webmail--------東吳信箱登入處\n https://webmail.scu.edu.tw/index.htm \n10. 東吳大學雲端圖書館查詢系統----借書、找文獻\n http://www.library.scu.edu.tw/ \n11. 東吳大學歷年課程資料及各學系師資資訊--輔系修什麼?\n http://www.scu.edu.tw/~curr/p3-2cos.htm \n12. 東吳大學訂餐系統----防疫小幫手 \n https://scu.nidin.shop/  "
    )
    line_bot_api.reply_message(event.reply_token, message)


def scu_space(event):
    message = ImageSendMessage(
        original_content_url="https://i.imgur.com/kSwxYdk.png",
        preview_image_url="https://i.imgur.com/kSwxYdk.png"
    )
    line_bot_api.reply_message(event.reply_token, message)


def space(event):
    message = TextSendMessage(  # 快速表單
        text='請選擇登記方式',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="網路登記", text='網路登記')),
                QuickReplyButton(
                    action=MessageAction(label="人工劃記", text='人工劃記')),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


def space_handwrit(event):  # 轉盤樣板
    message = TemplateSendMessage(
        alt_text='人工劃記',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='Q棟教師研究二樓',
                    text='填寫Q201門口的劃記表',
                    actions=[
                        URITemplateAction(
                            label='在哪裡',
                            uri='https://reurl.cc/GmxYEx'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='圖書館非書資料室',
                    text='至非書資料庫櫃台填寫登記表',
                    actions=[
                        URITemplateAction(
                            label='在哪裡',
                            uri='https://reurl.cc/0jpepl'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='各系專用研討室',
                    text='請至各系辦詢問',
                    actions=[
                        URITemplateAction(
                            label='在哪裡',
                            uri='https://reurl.cc/R0roXe'
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


def space_online(event):
    message = TemplateSendMessage(
        alt_text='網路登記',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='D棟學習進行室',
                    text='D509 分為完成室(2-4人)、未來室(4-8人)、藍沙發(3-6人)、現在室(2-4人)',
                    actions=[
                        MessageTemplateAction(
                            label='查看租借情況',
                            text='我想查看【D棟學習進行室】的租借情況'
                        ),
                        URITemplateAction(
                            label='前往預約',
                            uri='https://booking.scu.edu.tw/booking/Home'
                        ),
                    ]
                ),
                CarouselColumn(
                    title='R棟線上學習進行室',
                    text='R0210線上學習進行室分為L1、L2兩間會議室',
                    actions=[
                        MessageTemplateAction(
                            label='查看租借情況',
                            text='我想查看【R棟會議室】的租借情況'
                        ),
                        URITemplateAction(
                            label='前往預約',
                            uri='https://bigdata.scu.edu.tw/mrb/'
                        ),
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


def space_online_D(event):
    message = TemplateSendMessage(
        alt_text='D棟租借情況',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='D棟學習進行室',
                    text='D509 分為完成室(2-4人)、未來室(4-8人)、藍沙發(3-6人)、現在室(2-4人)',
                    actions=[
                        MessageAction(
                            label='完成室(2~4人)',
                            text='完成室預約情況'
                        ),
                        MessageAction(
                            label='未來室(4-8人)',
                            text='未來室預約情況'
                        ),
                        MessageAction(
                            label='現在室(2-4人)',
                            text='現在室預約情況'
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


CLIENT_ID = "B114815e13bb751"  # 申請 Imgur API取得ID


def R():
    driver = webdriver.Chrome(
        "C:/Users/austi/python/chromedriver")  # 本機上執行自動化模擬
    driver.get('https://bigdata.scu.edu.tw/mrb/')  # 取得R210空間租借網址
    driver.maximize_window()  # 放大螢幕
    time.sleep(2)  # 待機暫停
    driver.save_screenshot(
        "C:/Users/austi/python/spaceR.png")  # 截圖
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(
        "C:/Users/austi/python/spaceR.png", title="R210的資料")  # 將圖片上傳至imgur
    driver.quit()  # 關閉瀏覽器
    return uploaded_image.link  # return傳出連結，放在linebot圖片連結處


def space_online_D1(event):

    message = ImageSendMessage(
        original_content_url=space1(),
        preview_image_url=space1()
    )
    line_bot_api.reply_message(event.reply_token, message)


def space_online_D2(event):
    message = ImageSendMessage(
        original_content_url=space2(),
        preview_image_url=space2()
    )
    line_bot_api.reply_message(event.reply_token, message)


def space_online_D3(event):
    message = ImageSendMessage(
        original_content_url=space3(),
        preview_image_url=space3()
    )
    line_bot_api.reply_message(event.reply_token, message)


def space_online_R(event):
    message = ImageSendMessage(
        original_content_url=R(),
        preview_image_url=R()
    )
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == '__main__':
    app.run()
