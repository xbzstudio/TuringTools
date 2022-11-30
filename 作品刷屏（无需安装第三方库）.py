from urllib.request import *
from urllib.parse import *
import json
url=input('你要刷的网址:')
url=urlparse(url)[2].split('/')[2]
cookies=[]
while True:
    cookies.append(input('输入你要使用的第{zh}个账号的cookie（输入done结束）：'.format(zh=len(cookies)+1)))
    if cookies[-1]=='done':
        cookies.remove('done')
        break
print(cookies)
song='''都是勇敢的
你额头的伤口你的不同你犯的错
都不必隐藏
你破旧的玩偶你的面具你的自我
他们说要带着光驯服每一头怪兽
他们说要缝好你的伤没有人爱小丑
为何孤独不可光荣
人只有不完美值得歌颂
谁说污泥满身的不算英雄
爱你孤身走暗巷
爱你不跪的模样
爱你对峙过绝望
不肯哭一场
爱你破烂的衣裳
却敢堵命运的枪
爱你和我那么像
缺口都一样
去吗 配吗 这褴褛的披风
战吗 战啊 以最卑微的梦
致那黑夜中的呜咽与怒吼
谁说站在光里的才算英雄
他们说要戒了你的狂
就像擦掉了污垢
他们说要顺台阶而上而代价是低头
那就让我不可乘风
你一样骄傲着那种孤勇
谁说对弈平凡的不算英雄
爱你孤身走暗巷
爱你不跪的模样
爱你对峙过绝望
不肯哭一场
爱你破烂的衣裳
却敢堵命运的枪
爱你和我那么像
缺口都一样
去吗 配吗 这褴褛的披风
战吗 战啊 以最卑微的梦
致那黑夜中的呜咽与怒吼
谁说站在光里的才算英雄
你的斑驳与众不同
你的沉默震耳欲聋
You Are The Hero
爱你孤身走暗巷
爱你不跪的模样
爱你对峙过绝望
不肯哭一场 (You Are The Hero)
爱你来自于蛮荒
一生不借谁的光
你将造你的城邦
在废墟之上
去吗 去啊 以最卑微的梦
战吗 战啊 以最孤高的梦
致那黑夜中的呜咽与怒吼
谁说站在光里的才算英雄'''.replace('\n','鸡').split('鸡')
i=0
j=0
print('已开始刷屏，若想停止请关闭程序')
while True:
    http=json.loads(urlopen(Request('https://icodeshequ.youdao.com/api/works/comment',('{"id":"'+str(url)+'","content":"'+str(song[i])+'"}').encode('utf-8'),headers={'Accept': 'application/json, text/plain, */*','Content-Type': 'application/json','Cookie':cookies[j],'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.33'},method='POST')).read())
    if http['code']==0:
        i+=1
        if i==len(song):
            i=0
    j+=1
    if j==len(cookies):
        j=0
