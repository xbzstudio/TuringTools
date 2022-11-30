#本作品作者为qqcd，请勿抄袭
#编辑器：Visual Studio Code 即vs code
import urllib.request as ur
import json


class html():
    Html={      #用于储存主题的html代码。如果自建主题，需要自己动手写html、css和js
        'qqcd官方主题':{'css定义':'''<style>
    .work
    {  
        border-style:outset;
        border-color:blue;  
    }
    p{
        font-family:"幼圆";
    }
    h1{
        font-family:"幼圆";
    }
    h2{
        font-family:"幼圆";
    }
    h3{
        font-family:"幼圆";
    }
    h4{
        font-family:"幼圆";
    }
    h5{
        font-family:"幼圆";
    }
    a:link {color:#103787;text-decoration:none;border-style:outset;}      /* 未访问链接*/
    a:visited {color:#147fd7;text-decoration:none;border-style:outset;}  /* 已访问链接 */
    a:hover {color:#d63f3f;text-decoration:none;border-style:inset;}  /* 鼠标移动到链接上 */
    a:active {color:#931212;text-decoration:none;border-style:outset;}  /* 鼠标点击时 */
    #web_bg{
    position:fixed;
    top: 0;
    left: 0;
    width:100%;
    height:100%;
    min-width: 1000px;
    z-index:-10;
    zoom: 1;
    background-color: #fff;
    background-repeat: no-repeat;
    background-size: cover;
    -webkit-background-size: cover;
    -o-background-size: cover;
    background-position: center 0;
    }
    #qk{
        text-align:center;
        background-color:white;
        background-color:rgba(255,255,255,0.7);
    }
</style>
''','头':'''<meta charset="utf-8"></meta>
<title>{pageTitle}</title>
''','身':'''<div class="wrapper">
    <!--背景图片-->
    <div id="web_bg" style="background-image: url({bgimg});"></div>
    <!--其他代码 ... -->
    <div id="qk">
        <img src="{head}" height="120" width="120"></img>
        <h1>{bigTitle}</h1> 
        <h4>{icodeIntro}</h4>
        <p style="color:#696969">{pageIntro}</p>
        <h3>联系我！</h3>
        <p><a href="{icodePage}">我的小图灵主页</a></p>
        <h3>我的个人数据</h3>
        <h3 style="border-style:outset">点赞：{dz}||收藏：{sc}||被改编数：{gb}||被浏览量：{ll}</h3>
    </div>
    <br></br>
    <div id="qk">
        <h3>我的精选作品(共{workn}个作品)</h3>
        <p>---------------------------------------</p>
        <h3>若想观看所有作品，请前往我的小图灵主页。欢迎欣赏和点赞！！</h3>
        {works}
    </div>
    <div id="qk"><h3>已经到底啦~</h3></div>
    </div>
''','js代码':''}}


#生成主页的写入顺序是：头->css定义->身->js代码，这里我没有写js，如果想要整更多好玩的，去改写入函数(page_init)


class page():   #定义类
    data=None       #初始化用户信息为None
    pageData=None
    theme='qqcd官方主题'   #设定默认主题。如果你想要设置你的主题，可以通过更改html类的字典来设置，但是format要对的上
    def __init__(self,uid,paged={'pageTitle':'myPage','backboard_img':'https://pic.stackoverflow.wiki/uploadImages/121/32/48/171/2022/08/11/16/56/d2c411e7-f6fa-4def-bbcc-a8de7b4f13ef.png','bigTitle':'我的主页','pageIntro':'该程序作者：qqcd，严禁抄袭'},th='qqcd官方主题'):            #初始化函数
        self.data=json.loads(ur.urlopen('https://icodeshequ.youdao.com/api/user/index/hisStatics?userId={uid}'.format(uid=uid)).read())['data'] #读取后转为dict，将重要信息取出
        self.pageData=paged
        self.theme=th
    def page_init(self,html,lj=''):   #生成主页
        file=open(str(lj)+str(self.data['nickName'])+str('的个人主页.html'),'w',encoding='utf-8')
        file.write(html.Html[self.theme]['头'].format(pageTitle=self.pageData['pageTitle']))
        file.write(html.Html[self.theme]['css定义'])
        works=json.loads(ur.urlopen(str('https://icodeshequ.youdao.com/api/user/works/hisWorksList?page=1&size=20&userId=')+self.data['userId']).read())['dataList']
        workhtml=''  #读取第一页的作品信息，并生成html代码
        for i in range(len(works)):
            workhtml+='<a href="{wz}"><div class="work" style="vertical-align:middle; "><img src="{img}" height="184" width="184"></img><h3>{workName}</h3></div></a>\n'.format(wz=str('https://icodeshequ.youdao.com/work/')+str(works[i]['id']),img=works[i]['imgUrl'],workName=works[i]['title'])

        file.write(html.Html[self.theme]['身'].format(head=self.data['img'],bgimg=self.pageData['backboard_img'],bigTitle=self.pageData['bigTitle'],icodeIntro=self.data['intro'],pageIntro=self.pageData['pageIntro'],icodePage=str('https://icodeshequ.youdao.com/personal?userId=')+str(self.data['userId']),dz=self.data['praiseNum'],sc=self.data['enshrinesNum'],gb=self.data['forkNum'],ll=self.data['viewNum'],workn=self.data['worksNum'],works=workhtml))
        file.write(html.Html[self.theme]['js代码'])
        file.close()
