import asyncio
import urllib3 , time , json , urllib.request

async def view(manager,url):
       loop=asyncio.get_event_loop()
       await loop.run_in_executor(None,manager.request,'GET','https://icodeshequ.youdao.com/api/works/detail?id={ID}'.format(ID=url))

def getId(site):
    return site[site.index('work/')+5:site.find('?from='):1] if site.find('?from=')>-1 else site[site.index('work/')+5::1]

if __name__ == '__main__':
       start=time.time()
       tacks=[]
       http=urllib3.PoolManager()
       url=getId(input('输入目标作品网址：'))
       count=int(input('你要刷的浏览量：'))
       for i in range(int(count*1.25/100)):
              tacks+=[view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url),view(http,url)]
              print('协程部署进度:',(i+1)*100,'/',int(count*1.25))
       count=json.loads(urllib.request.urlopen(f'https://icodeshequ.youdao.com/api/works/detail?id={url}').read())['data']['browseNum']
       print('协程部署完成，已开始刷浏览')
       print('请耐心等待至IDLE输出>>>')
       print('协程的完成结果绝对会比原本数值所部署的要少，所以我们加多了部署量')
       loop=asyncio.get_event_loop()
       loop.run_until_complete(asyncio.wait(tacks))
       print('用时：',time.time()-start,'/ 平均每秒：',int(json.loads(urllib.request.urlopen(f'https://icodeshequ.youdao.com/api/works/detail?id={url}').read())['data']['browseNum']-count)/(time.time()-start),'/ 实际已刷：',json.loads(urllib.request.urlopen(f'https://icodeshequ.youdao.com/api/works/detail?id={url}').read())['data']['browseNum']-count)
       loop.close()
