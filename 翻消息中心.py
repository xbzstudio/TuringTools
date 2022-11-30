import requests
i=258
while True:
    site='https://icodeshequ.youdao.com/api/user/message/commentMessage?page={page}&size=10'.format(page=str(i))
    data=requests.get(url=site,headers={'cookie':'OUTFOX_SEARCH_USER_ID_NCOO=329695129.0663486; OUTFOX_SEARCH_USER_ID="-263173256@10.110.96.160"; P_INFO=m3366487826@163.com|1659607896|0|youdaodict|00&99|fuj&1659512742&youdaodict#gud&440100#10#0#0|&0|ke&mail163&youdaodict|m3366487826@163.com; DICT_PERS=v2|urscookie||DICT||web||604800000||1659607896992||240e:3b3:71:7c30:a1bd:f2d3:adc:bd7a||m3366487826@163.com||gKhMzW6MYE0JBOLpFhHT40PZhMUEOf6u0QFnLOW0HpLRwK0LYERfOMR6Z64Ul0LTB0wBhfe4nMzm0QLnfquRLPLR; wap_abtest=5; hb_MA-BF02-71D44E7C0390_source=icode.youdao.com; DICT_SESS=v2|i91dkmKVORgKh4QBhH6yRgykLkG0MwZ0TB0fez6LOW0OfkLOMnfT4Rwz0H6Lh4PS0JSO4zY64QL0OEhMTBRfwBRlA6LqyhHwF0; DICT_LOGIN=3||1659779824490; xiaotuling=icode%3Asession%3A6e39964956379b86453b1cea79409a8d; JSESSIONID=abc0vgIJFGBEa83dBx4jy'}).text
    print("page{y},site:{s}\n".format(y=str(i),s=site))
    while 'actionUserId' in data:
        data=data[data.find('actionUserId')+15::]
        print(data[0:data.find('",'):1],end="    ")
        data=data[data.find('content')+10::]
        print(data[0:data.find('",'):1])
    i+=1
    print("\n\n\n\n",end="")
    input("")
