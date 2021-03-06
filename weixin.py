import web
import time
import xml.etree.ElementTree
urls=(
'/','index'
)
app=web.application(urls,globals())

class index:
  def GET(self):
    print web.input()
    params=web.input()
    signature=params.signature if hasattr(params, "signature") else ""
    echostr=params.echostr if hasattr(params, "echostr") else ""
    return echostr
  def POST(self):
    print web.input()
    print web.data()
    params=web.input()
    openid=params.openid if hasattr(params, "openid") else ""
    data=web.data()

    root = xml.etree.ElementTree.XML(data)
    toUserName= root.findall("ToUserName")
    fromUserName= root.findall("FromUserName")
    content= root.findall("Content")

    retXml=u"""
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%d</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    </xml>
    """
    retXml=retXml % (fromUserName[0].text,toUserName[0].text,int(round(time.time())),content[0].text)

    print retXml.encode("utf-8")
    return retXml


if __name__=="__main__":
  app.run()

