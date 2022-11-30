import urllib.request
import turtle
turtle.penup()
turtle.goto(-380,300)
site=input("输入你要查询的作品网址")[-32::]
site2='https://icodeshequ.youdao.com/api/works/detail?id='+site
print("源网址："+site2)
site2=urllib.request.urlopen(site2).read()

n=0#当前所读 

k=0#列表所读 

strr=""  #储存

a=['"id":','"title":','"imgUrl":','"description":','"type":','"userId":','"status":','"likeNum":','"browseNum":','"enshrineNum":','"code":','"userName":','"userImage":','"forkId":','"haveLiked":','"haveEnshrined":','"createTimeStr":','"updateTimeStr":','"codeLanguage":','"shortLink":','"theme":','"subTheme":','"iframeUrl":','"scratchFile":','"codeType":','"firstPopups":','"forkAuthorizationStatus":','"isFirstPublish":','"haveReported":']
b=["作品ID：","标题：","封面储存在小图灵图床的位置：","简介：","类型：","发布者ID：","地位：","点赞量：","浏览量：","收藏量：","该作品的源码地址（仅sc作品适用）：","发布者昵称：","发布者头像储存在小图灵图床的位置：","改编ID(为空则代表原创)：","你的账号给该作品点过的赞数：","你的账号给该作品点过的收藏数：","发布时间：","更新时间：","代码语言：","在分享端的作品网址：","主题：","子主题：","作品在展示页所iframe的展示网址：","scratch文件：","源码格式：","第一个弹出窗口（不是为1是为0）：","是否允许改编（不是为1是为0）：","这个作品是否首次发布：","是否已被你的账号举报（0为未举报1为已举报）："]
for i in range(len(site2)):
    if not k==len(a):
        if not n==len(a[k]):
            if site2[i]==a[k][n]:
                strr=""
                n+=1
            else:
                strr="" 
        else:
            strr=strr+site2[i]
            if a[k]=='"code":':
                strr=""
            if (site2[i+1]==',' and site2[i+2]=='"') or (a[k]=='"haveReported":' and site2[i+1]=="}"):
                n=0
                k+=1
                if a[k-1]=='"code":':
                    strr=""
                    print(b[k-1]+'https://icode.youdao.com/scratch/project/'+site)
                    turtle.write(b[k-1]+'https://icode.youdao.com/scratch/project/'+site,align="left",font=("宋体",10,"normal"))
                    turtle.goto(-380,300-k*15)
                else:
                    print(b[k-1]+strr)
                    turtle.write(b[k-1]+strr,align="left",font=("宋体",10,"normal"))
                    turtle.goto(-380,300-k*15)
