import requests
import time
import datetime
import socket
import uuid
 
def test():
    headers = {
    'Host': 'connect.rom.miui.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    }
    res=requests.get('http://connect.rom.miui.com/generate_204,headers=headers')
    return res
 
 
 
def weblogin(user,password,IP,mac):
    headers = {
    'Host':'172.17.0.2:801',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive',
    'Referer':'http://172.17.0.2/',
    'Upgrade-Insecure-Requests':'1'
    }
     
     
     
     
    url='http://172.17.0.2:801/eportal/?c=ACSetting&a=Login&loginMethod=1&protocol=http:&hostname=172.17.0.2&port=&iTermType=1&wlanuserip={1}&wlanacip=210.36.18.65&wlanacname=ME60-1&redirect=null&session=null&vlanid=0&mac={0}&ip={1}&enAdvert=0&jsVersion=2.4.3&DDDDD=,0,{2}&upass={3}&R1=0&R2=0&R3=0&R6=0¶=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login='.format(mac,IP,user,password)
    backinfo=requests.get(url,headers=headers)
 
def getip():
    return socket.gethostbyname(socket.gethostname())
 
def getmac():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return "-".join([mac[e:e+2] for e in range(0,11,2)])
 
 
 
 
count=0
ccc=0
dd=0
ee=0
while 1==1:
    time.sleep(0.25)
    if str(test())=='<Response [200]>':
        ccc+=1
        print("Lost Connect{}".format(ccc))
        if ccc==2:
            weblogin('账号','密码',str(getip()),str(getmac()))
            print('Relogin')
    else:
        if dd==20:
            dd=0
            ee+=1
            print("Internet is OK {}".format(ee))
        dd+=1
        ccc=0
