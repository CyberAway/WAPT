#!/usr/bin/python3
import os, sys
import random


def clear():
    os.system("clear")
    
def banner():
    add =["""
'########::'########:'##::::'##:'########:'########:::'######::'########:'########::'##::: ##::'######::
 ##.... ##: ##.....:: ##:::: ##: ##.....:: ##.... ##:'##... ##: ##.....:: ##.... ##: ###:: ##:'##... ##:
 ##:::: ##: ##::::::: ##:::: ##: ##::::::: ##:::: ##: ##:::..:: ##::::::: ##:::: ##: ####: ##: ##:::..::
 ########:: ######::: ##:::: ##: ######::: ########::. ######:: ######::: ##:::: ##: ## ## ##:. ######::
 ##.. ##::: ##...::::. ##:: ##:: ##...:::: ##.. ##::::..... ##: ##...:::: ##:::: ##: ##. ####::..... ##:
 ##::. ##:: ##::::::::. ## ##::: ##::::::: ##::. ##::'##::: ##: ##::::::: ##:::: ##: ##:. ###:'##::: ##:
 ##:::. ##: ########:::. ###:::: ########: ##:::. ##:. ######:: ########: ########:: ##::. ##:. ######::
..:::::..::........:::::...:::::........::..:::::..:::......:::........::........:::..::::..:::......:::
    """, """
           __  ___           __   __       ___  __   __       
|  |  /\  |__)  |     __    /  ` /  \ |\ |  |  |__) /  \ |    
|/\| /~~\ |     |           \__, \__/ | \|  |  |  \ \__/ |___ 
                                                              """, """
  @@@@@@@  @@@@@@  @@@@@@@  @@@@@@@@ @@@@@@@  @@@ @@@       @@@@@@   @@@@@@   @@@@@@   @@@@@@ 
 !@@      @@!  @@@ @@!  @@@ @@!      @@!  @@@ @@! !@@      @@   @@@ @@!  @@@ @@   @@@ @@   @@@
 !@!      @!@  !@! @!@  !@! @!!!:!   @!@!@!@   !@!@!         .!!@!  @!@  !@!   .!!@!    .!!@! 
 :!!      !!:  !!! !!:  !!! !!:      !!:  !!!   !!:         !!:     !!:  !!!  !!:      !!:    
  :: :: :  : :. :  :: :  :  : :: ::: :: : ::    .:         :.:: :::  : : ::  :.:: ::: :.:: :::"""]
    print(random.choice(add))
   
def information_developer():
    print("""
8888888b.                                         8888888888 
888   Y88b                                        888        
888    888                                        888        
888   d88P 888d888 .d88b.  .d8888b  .d8888b       8888888    
8888888P"  888P"  d8P  Y8b 88K      88K           888        
888        888    88888888 "Y8888b. "Y8888b.      888        
888        888    Y8b.          X88      X88      888        
888        888     "Y8888   88888P'  88888P'      888        
                                                             """)
    
    print("[*] Telegram - @CyberAway")
    print("version: 0.1")
    print("")
    print("")
    print("Тулза была создана для автоматизации рутины!")
    print("Сильно не поможет, но многое упростит.")







def setup_local():
    file_path = '/usr/bin/WAPT.py'
    pwd = os.path.exists(file_path)
    if pwd == False:
        print("Установить WAPT локально?")
        print("После вы сможете запускать тулзу по команде из любой директории: WAPT")
        action = input("Y or N #: ")
        clear()
        if action == "Y":
            os.system('echo "$(sudo mv WAPT.py /usr/bin/WAPT.py)"')
            os.system('echo "$(sudo chmod +x /usr/bin/WAPT.py)"')
            os.system('echo "$(ln -s /usr/bin/WAPT.py /usr/bin/WAPT)"')
            print("Успешно установлен!")
            print("Попробуйте запустить меня командой: WAPT из любого места!")
        else:
            exit()
    else:
        pass





def fuzz_files():
    fuzzing = {
        "folders" : "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt",
        "files" : "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt",
        "parametr" : "/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt",
        "login" : "/usr/share/seclists/Usernames/top-usernames-shortlist.txt",
        "names" : "/usr/share/seclists/Usernames/Names/names.txt",
        
    }
    passwords = {
        "1.000" : '/usr/share/seclists/Passwords/xato-net-10-million-passwords-1000.txt',
        "10.000" : '/usr/share/seclists/Passwords/xato-net-10-million-passwords-10000.txt',
        "100.000" : '/usr/share/seclists/Passwords/xato-net-10-million-passwords-100000.txt',
        "1.000.000" : '/usr/share/seclists/Passwords/xato-net-10-million-passwords-1000000.txt',
        "rockyou" : '/usr/share/seclists/Passwords/rockyou.txt',
    }
    print("Введите адрес: https://example.com/")
    domain = input("[-] URL: ")
    clear()
    
    print("[-] Выберите что будете фаззить")
    print("[1] - Папки")
    print("[2] - Файлы")
    print("[3] - Параметры")
    print("[4] - Параметры")
    print("[5] - Логины и пароли")
    
    action = input("#: ")
    clear()
    
    
    if action == "1":
        os.system('echo "$(ffuf -u {0}FUZZ -c -w {1} -t 1000 -mc 200)"'.format(domain, fuzzing["folders"]))
    elif action == "2":
        os.system('echo "$(ffuf -u {0}FUZZ -c -w {1} -e .php,.html,.txt  -t 1000 -mc 200)"'.format(domain, fuzzing["files"]))
    elif action == "3":
        os.system('echo "$(ffuf -u {0}FUZZ -c -w {1} -t 1000 -mc 200)"'.format(domain, fuzzing["parametr"]))
    else:
        clear()

def domain_info():
    print("Введите домен в формате: codeby.net")
    domain = input("[-] Domain: ")
    clear()
    
    os.system('echo "$(whois {0})"'.format(domain))
    os.system('echo "$(nslookup {0})"'.format(domain))
    os.system('echo "$(host {0})"'.format(domain))
    
    
def reverseDNS():
    print("Введите IP в формате: 111.111.111")
    ip = input("[-] IP #: ")
    clear()
    
    print("Введите IP Range 0<255")
    a =  input("[-] 0<255: ")
    clear()
    
    print("Введите IP Range 0>255")
    b = input("[-] 0>255: ")
    clear()
    for i in range(int(a), int(b)):
        full_ip = str(ip)+"."+str(i)
        os.system('echo "{0} $(dig -x {0} +short)"'.format(full_ip))
    

def menu():
    banner()
    print("[---------------------------------]")
    print("[1] - REVERSE DNS")
    print("[2] - Domain info")
    print("[3] - AUTO Fuzzing")
    print("[DEV] - Developer")
    print("[CLEAR] - Clear Console")
    print("[EXIT] - EXIT Tools")
    print("[---------------------------------]")
    action = input("#: ")
    clear()
    
    if action == "1":
        try:
            reverseDNS()
        except:
            clear()
            menu()
    elif action == "2":
        try:
            domain_info()
        except:
            clear()
            menu()
    elif action == "3":
        try:
            fuzz_files()
        except:
            clear()
            menu()
    elif action == "DEV":
        information_developer()
    elif action == "CLEAR":
        clear()
    elif action == "EXIT":
        exit()
    else:
        exit()


if __name__ == "__main__":
    setup_local()
    while True:
        menu()


