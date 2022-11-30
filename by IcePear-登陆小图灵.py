import requests
import json
import warnings


class LoginWarning(Warning):
    """Cannot login"""


def strcookies_to_dict(strcookies):
    return {i.split("=", 1)[0].strip(): i.split("=", 1)[-1].strip() for i in strcookies.split(";")}


class Turing:
    def __init__(self, cookie=None):
        r'''
        传入一个cookie字典登录小图灵。
        经过检测，只传入DICT_PERS一个参数即可登录小图灵
        例如：

        >>> import turingio
        >>> XiaoMing = turingio.Turing({'DICT_PERS': '******'})
        >>> XiaoMing.updateIntro("我最帅")

        登录后会进行检测
        如果登录失败会抛出LoginWarning
        '''
        self.__session = requests.Session()
        self.logincode = None
        if cookie != None:
            self.__session.cookies = requests.utils.cookiejar_from_dict(
                cookie)
        self.checklogin()
        self.__session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198"
        self.__session.headers['Host'] = "icodeshequ.youdao.com"
        self.__session.headers['Referer'] = "https://icodeshequ.youdao.com/"
        self.__session.headers['Sec-Fetch-Dest'] = "empty"
        self.__session.headers['Sec-Fetch-Mode'] = "cors"
        self.__session.headers['Sec-Fetch-Site'] = "same-origin"

    def checklogin(self):
        url = 'https://icodecontest-online-api.youdao.com/api/user/info'
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Host': 'icodecontest-online-api.youdao.com',
            'Origin': 'https://icodeshequ.youdao.com',
            'Referer': 'https://icodeshequ.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198'
        }
        check = self.__session.get(url=url, headers=headers).json()
        print(check)
        if check['code'] == 0:
            self.login = 'OK'
            self.encryptionId = check['data']['encryptionUserId']
            self.Id = check['data']['userId']
            self.name = check['data']['name']
            self.image = check['data']['image']
            self.permissions = check['data']['permissions']
            self.hasCourse = check['data']['hasCourse']
            self.userIdentity = check['data']['userIdentity']
            return(True)
        else:
            print(check)
            warnings.warn("Cannot Login", LoginWarning)
            return(False)

    def updateIntro(self, text):
        updateIntro = self.__session.post(
            url="https://icodeshequ.youdao.com/api/user/updateIntro",
            data=text.encode('utf-8'))
        #self.code = updateIntro.status_code
        return updateIntro.json()

#
#
#       请填入您的cookie在双引号内
print(strcookies_to_dict('''Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Cookie: OUTFOX_SEARCH_USER_ID_NCOO=1288917384.1164267; OUTFOX_SEARCH_USER_ID="288652133@10.108.162.134"; wap_abtest=6; xiaotuling=icode%3Asession%3A11cb1f09450990c2b8876e8895b2078c; DICT_FORCE=true; P_INFO=m3366487826@163.com|1659029049|0|youdaodict|00&99|jil&1658843705&youdaodict#gud&440100#10#0#0|&0|ke&youdaodict|m3366487826@163.com; DICT_SESS=v2|pdrPOwHvLWzAhHU5k4U50QKOMQZ0HTZ0zY6M6zhMgL0kEPLpL64O5RkW6LgyRLlfRqyhHzAhHz5R64PLqu0HlE0U5OMJZ0Lpy0; DICT_PERS=v2|urscookie||DICT||web||604800000||1659029049817||113.119.177.164||m3366487826@163.com||6L6MqLk4pBRpyOfUl6MwBRTZhMUfRMQL0PuOLw40HeLRT40MP4nMlA0wBO4QFnHOE0YfkfU5OfUERwFOMwS6LTz0; DICT_LOGIN=3||1659029049822
Host: icodecontest-online-api.youdao.com
Origin: https://icodeshequ.youdao.com
Referer: https://icodeshequ.youdao.com/
sec-ch-ua: " Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'))'''))
