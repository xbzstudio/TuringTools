import urllib.request
import urllib.parse
import json
def getProblemInfo(url):
       return (str(urllib.parse.urlparse(url)[2])+str(urllib.parse.urlparse(url)[-1])).split('/')[2::]
cookies=input('输入您的Cookie。如果您想让程序读取使用文档形式储存的cookie，请输入读取（确保您的文档中只有一行和一个cookie）：')
if cookies=='读取':
       cookies=open(input('文件路径：'),'r').read()
while True:
       url=input('输入您要破解答案的有道信息学题目网址（适用于上课用户）：')
       info=getProblemInfo(url)
       Json={
       "courseId":str(info[0]),
       "problemId":str(info[-1]),
       "lessonId":str(info[1]),
       "lessonProblemType":1
              }
       print('==============================================================')
       print('题目信息：',info)
       print('请求负载（json形式）：',Json)
       print('==============================================================\n\n')
       request=urllib.request.Request(url='https://icodecontest-online-api.youdao.com/api/course/lesson/problem/detail',data=json.dumps(Json).encode('utf-8'),headers={'Content-Type':'application/json;charset=UTF-8','Cookie':cookies},method='POST')
       xy=json.loads(urllib.request.urlopen(request).read())
       print(xy['data']['content'].replace('$//', '').replace('$','').replace('\\', '').replace('![](','（图片链接）'),'\n\n',xy['data']['analysis'].replace('$//', '').replace('![](','（图片链接）').replace('$','').replace('\\', ''))
       print('\n\n==============================================================')
       input('按下enter键继续浏览题目解析')
