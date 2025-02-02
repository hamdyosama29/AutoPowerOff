from datetime import datetime
from colorama import  Fore
import time
import os
while True:
    try:
        os.system('clear')
        datatime = datetime.now()
        strftime = datatime.strftime('%p')
        enter_hour = int(input(Fore.MAGENTA + 'Enter hour: '))
        enter_minute = int(input(Fore.MAGENTA + 'Enter minute: '))
        while True:
            enter_strftime = str(input(Fore.MAGENTA + 'Enter strftime AM / PM: ').upper() or strftime)
            if enter_strftime != 'AM' and enter_strftime != 'PM':
                print(Fore.RED + '----------------------------------------------')
                print(Fore.RED + 'Looks like you entered the timing incorrectly.')
                continue
            else:
                break
        enter_time = f'{enter_hour}:{enter_minute} {enter_strftime}'
        while True:
            datatime = datetime.now()
            strftime = datetime.now().strftime('%p')
            hour = datatime.hour
            minute = datatime.minute
            now = f'{hour}:{minute} {strftime}'
            os.system('clear')
            print(Fore.RED + 'Waiting for the time.')
            if enter_time == now:
                os.system('poweroff')
                break
            else:
                time.sleep(1)
                continue
    except:
        print(Fore.RED + 'Looks like you entered the timing incorrectly.')
        print(Fore.RED + '----------------------------------------------')
        time.sleep(1)
        os.system('clear')
        continue