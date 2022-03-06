import requests
import webbrowser
import os

mmWords=f"""\033[1m\033[32m1. Information about your device
2. Information adout IP-address
\033[35m\033[4m3. Support the author ♡ 
\033[24m\033[36mSelect one of the items: \033[4m\033[33m"""

saWords=f"""\033[1m\033[34m1. Discord
\033[36m2. Telegram
\033[31m3. YouTube
\033[32m4. Back
\033[24m\033[36mSelect one of the items: \033[4m\033[33m"""


def support(supvariant):
    try:
        if int(supvariant) <= 0 or int(supvariant) >= 5:
            print('\033[0m')
            os.system('cls' if os.name == 'nt' else 'clear')
            support(input(mmWords))
        else:
            if int(supvariant) == 1:
                url=f"https://discord.gg/d4qwZ4uz5n"
                webbrowser.open(url, new=2)
                print('\033[0m')
                os.system('cls' if os.name == 'nt' else 'clear')
                support(input(saWords))
            elif int(supvariant) == 2:
                url=f"https://t.me/psychoklub"
                webbrowser.open(url, new=2)
                print('\033[0m')
                os.system('cls' if os.name == 'nt' else 'clear')
                support(input(saWords))
            elif int(supvariant) == 3:
                url=f"https://www.youtube.com/c/t1rxdqq"
                webbrowser.open(url, new=2)
                print('\033[0m')
                os.system('cls' if os.name == 'nt' else 'clear')
                support(input(saWords))
            elif int(supvariant) == 4:
                print('\033[0m')
                os.system('cls' if os.name == 'nt' else 'clear')
                main_menu(input(mmWords))
            else:
                pass
    except:
        print('\033[0m')
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu(input(mmWords))
        
def user():
    usWords=f"""\033[1m\033[92mMACHINE:  \033[4m\033[94m\033[1m{os.uname().machine};\033[0m
\033[1m\033[92mNODENAME:  \033[4m\033[94m\033[1m{os.uname().nodename};\033[0m
\033[1m\033[92mRELEASE:  \033[4m\033[94m\033[1m{os.uname().release};\033[0m
\033[1m\033[92mSYSNAME:  \033[4m\033[94m\033[1m{os.uname().sysname};\033[0m
\033[1m\033[92mVERSION:  \033[4m\033[94m\033[1m{os.uname().version};\033[0m
\033[1m\033[32mGo back?  (y/n):  \033[0m\033[1m\033[4m\033[93m
"""
    gback=input(usWords)
    if gback == 'y':
        print('\033[0m')
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu(input(mmWords))
    else:
        print('\033[0m')
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\033[35mThanks for using ♡  ')
        
def ip(ip_add):    
    responseIP = requests.get('https://api64.ipify.org?format=json').json()
    ip_address = ip_add 
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    if response.get('error') == True:
        ip_address=responseIP["ip"]
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    for i in response:
        print(f'\033[92m{str(i).upper()}:  \033[4m\033[94m\033[1m{response.get(i)};\033[0m')
    if response.get('latitude') and response.get('longitude'):
        lat=str(response.get('latitude'))
        lon=str(response.get('longitude'))
        searchIp=input('\n\033[96mOpen browser?  (y/n) if "n" back:  \033[0m\033[1m\033[4m\033[93m')
        if searchIp=='y':
            url=f"https://maps.google.com/maps?q={lat}+{lon}&client=ms-android-hct&sxsrf=APq-WBsdMGbumlrSiADJZN6BwyA_iy1FQA:1646497897127&gs_lcp=ChNtb2JpbGUtZ3dzLXdpei1zZXJwEAM6BwgAEEcQsAM6BwgjEOoCECdKBAhBGABQxRBYxRBgtxhoAnACeACAAfgCiAGCBJIBBzAuMS4wLjGYAQCgAQGwAQ_IAQjAAQE&um=1&ie=UTF-8&sa=X&ved=2ahUKEwiBls2iuq_2AhUGmYsKHYSGDuoQ_AUoAXoECAEQAw"
            webbrowser.open(url, new=2)
            print('\033[0m')
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu(input(mmWords))
        else:
            print('\033[0m')
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu(input(mmWords))
            

def main_menu(variant):
    try:
        if int(variant) <= 0 or int(variant) >= 4:
            print('\033[0m')
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu(input(mmWords))
        else:
            if int(variant) == 1:
                print('\033[0m')
                os.system('cls' if os.name == 'nt' else 'clear')
            
                user()
            elif int(variant) == 2:
                print('\033[0m')
                os.system('cls' if os.name == 'nt' else 'clear')
            
                ip(input('\033[96mEnter IP-address to INFO (None = Your IP):  \033[0m\033[1m\033[4m\033[93m'))
            elif int(variant) == 3:
                print('\033[0m')
                os.system('cls' if os.name == 'nt' else 'clear')
            
                support(input(saWords))
    except:
        print('\033[0m')
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu(input(mmWords))

main_menu(input(mmWords))