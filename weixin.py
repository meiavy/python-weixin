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

    print root.findall("ToUserName")
    print root.findall("./ToUserName")
    #print root.findall("../xml/ToUserName")
    #print root.findall("//ToUserName")
    #xmlRoot

    """<xml><ToUserName><![CDATA[gh_a15e2f8bae8b]]></ToUserName>
    <FromUserName><![CDATA[oJtIMsxje0-7rt0S18WH2iIhkMNU]]></FromUserName>
    <CreateTime>1467180642</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[111dsfdsafsafasfd]]></Content>
    <MsgId>6301492875129622501</MsgId>
    </xml>"""



    str="""<xml>
    <ToUserName><![CDATA["""
    str+=openid
    str+="""]]></ToUserName>
    <FromUserName><![CDATA["""
    str+="gh_a15e2f8bae8b"
    str+="""]]></FromUserName>
    <CreateTime>"""
    str+=int(round(time.time())).__str__()
    str+="""</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[1111111111]]></Content>
    </xml>"""
    print str
    return str


if __name__=="__main__":
  app.run()

