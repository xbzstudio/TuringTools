
#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import requests #需要安装requests

import json
if __name__ == '__main__':
  file_name = r"C:\Users\33664\Desktop\魔法少女小圆第一集在线观看.svg" #你要打开的
  with open(file_name, 'rb') as fp:
      fdata = fp.read()
 
  url="https://tiku-outside.youdao.com/nos/scratch/asset/aa.svg/" #目标为bingli_site_0_03.svg
  req=requests.post(url=url,data=fdata)
  a=json.loads(req.text)
  print(a)
  if a['code']=='200':
    print("200 OK")
  print(a['message'])
  if a['code']=='200':
    print('http://ydschool-online.nosdn.127.net/'+a['data']['key'])
  
  
