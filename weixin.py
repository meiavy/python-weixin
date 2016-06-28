import web
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
    str="""<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
        <CreateTime>12345678</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[1]]></Content>
        </xml>"""

if __name__=="__main__":
  app.run()

