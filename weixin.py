import web
import datetime
urls=(
'/','index'
)
app=web.application(urls,globals())

class index:
  def GET(self):
    print web.input()
    params=web.input()
    signature=params.signature
    echostr=params.echostr
    return echostr
  def POST(self):
    print web.input()
    params=web.input()
    openid=params.openid
    str="""<xml>
    <ToUserName><![CDATA["""
    str+=openid
    str+="""]]></ToUserName>
    <FromUserName><![CDATA["""
    str+="magicheartman"
    str+="""]]></FromUserName>
    <CreateTime>"""
    str+=datetime.time.microsecond/1000;
    str+="""</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[1111111111]]></Content>
    </xml>"""
    return str


if __name__=="__main__":
  app.run()

