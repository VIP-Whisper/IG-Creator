import requests,random,base64
from uuid import uuid4 as uid
from user_agent import generate_user_agent as ua
csrf=input('csrf token (get it from console) : ')
email=input('email : ')
user='whisper'+str(random.randint(10000,99999))
bd=random.randint(1,28)
bm=random.randint(1,12)
by=random.randint(1999,2003)
cid='ZSZsJAABAAGYl25zFiOlQMw-G7Wq'
head={"Host": "www.instagram.com","content-length": "370","sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"","x-ig-www-claim": "0","sec-ch-ua-platform-version": "\"\"","x-requested-with": "XMLHttpRequest","dpr": "2","sec-ch-ua-full-version-list": "\"Not_A Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"120.0.6099.116\", \"Google Chrome\";v=\"120.0.6099.116\"","x-csrftoken": "2ppNQ4cFnrapD2LxLwUGY8pkTkz3d9dL","sec-ch-ua-model": "\"\"","sec-ch-ua-platform": "\"Linux\"","x-ig-app-id": "936619743392459","sec-ch-prefers-color-scheme": "light","sec-ch-ua-mobile": "?0","x-instagram-ajax": "1010615039","user-agent": str(ua()),"viewport-width": "980","content-type": "application/x-www-form-urlencoded","accept": "*/*","x-asbd-id": "129477","origin": "https://www.instagram.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.instagram.com/accounts/emailsignup/","accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5,zh-CN;q=0.4,zh;q=0.3"}
co={"cookie":f"ig_did={uid()}; ig_nrcb=1; csrftoken={csrf}; mid={cid}; datr=EWmaZaOgkIyxdpn-fqu6von3"}
data=f'enc_password=%23PWD_INSTAGRAM_BROWSER%3A10%3A1703990307%3AAXVQAC2vMbosCujHFUVgh2tJuiJZSF0TmesSmKzZUq4I9bo%2BIAw3KfoQ7xPEtWQ9o9Nw%2BlbVzzvNCLnC1uKxtZTY%2F%2FTSZ85prAThJLQCuFMdourZCpBRpywKe%2BDF0VgE7W72kWKc5Cw6tvcci7E%3D&email={email}&first_name=Whisper+Legendary&username={user}&client_id={cid}&seamless_login_enabled=1&opt_into_one_tap=false'
res=requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',data=data,headers=head,cookies=co).text
if '"dryrun_passed":true' in res:
 pass
else:
 print(res)
send=requests.post('https://www.instagram.com/api/v1/accounts/send_verify_email/',data=f'device_id=ZSZsJAABAAGYl25zFiOlQMw-G7Wq&email={email}',headers=head,cookies=co).text
if '"email_sent":true' in send:
 pass
else:
 print(send)
 exit()
otp=input('otp : ')
sc=requests.post('https://www.instagram.com/api/v1/accounts/check_confirmation_code/',data=f'code={otp}&device_id=ZSZsJAABAAGYl25zFiOlQMw-G7Wa&email={email}',headers=head,cookies=co).json()
try:
    scode=sc['signup_code']
except:
    print(sc)
    exit()
com=requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',data=f'enc_password=%23PWD_INSTAGRAM_BROWSER%3A10%3A1703990364%3AAXVQADMJFMj1YW0Td%2BUYu0%2BlttQhFRHWyKLuXoxe%2Ba8i94o5C2CtiePOmxSAZ8nNKT6G9X%2B1mHJGuXWWItbpZopqDh3ljSTxtNSNglX08gD6jbuztBd0du%2FW3%2F53EqiMzWK9o3wB%2B50jfNLSxVE%3D&day={bd}&email={email}&first_name=Whisper+Legendary&month={bm}&username={user}&year={by}&client_id={cid}&seamless_login_enabled=1&tos_version=row&force_sign_up_code={scode}',headers=head,cookies=co)
if com.status_code == 572:
    s=requests.post('https://i.instagram.com/api/v1/accounts/login/',data='signed_body=d1dec9e0696a8e2a80de92a5d5d2125f25c5a9b16365f114d38868fc2eb4cdbb.{"reg_login":0,"password":"whisper666","device_id":"2c993011-1ddc-4076-810e-925b2f909cb4","username":"'+user+'","adid":"e2798430-cf08-46e6-ab2a-9146c0edb0d7","login_attempt_count":0,"phone_id":"2c993011-1ddc-4076-810e-925b2f909cb4"}&ig_sig_key_version=5',headers={"Host": "i.instagram.com","accept-language": "en;q\u003d1","user-agent": "Instagram 118.0.0.28.122 (iPhone5.2; iOS 10_15; en; en_US; scale\u003d2.61; gamut\u003dnormal; 978*2119; 181496429) AppleWebKit/420+","x-ig-connection-type": "WiFi","x-ig-capabilities": "36r/dw\u003d\u003d","x-ig-app-id": "124024574287414","x-ig-abr-connection-speed-kbps": "0","x-ig-bandwidth-speed-kbps": "0.000","x-ig-connection-speed": "0kbps","x-fb-http-engine": "Liger","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","content-length": "331","accept-encoding": "gzip"})
    try:
     sid=s.cookies['sessionid']
     pk=s.cookies['ds_user_id']
     print(f'[√] Created : {email} | whisper666 | {user} | {pk} | {sid}')
     with open('IG-Acc.txt','a+') as ig:
      ig.write(f'{email}:whisper666:{sid}:{pk}:{user}\n')
    except:
     print(s.text)
else:
    print(com.text)
    print(com.status_code)
