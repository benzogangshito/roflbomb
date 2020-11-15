import os
import time
banner = '''
    ____    coder: @benzogangshito 
→_→ |Ermux         ←_←
→_→ |   |\  /|     ←_←
→_→ |   | \/ |ozga ←_←      
 
Это мой первый скрипт! 
Канал в телеграмме: @blackhacker101
Телеграмм: @benzogangshito
              
'''
def main():
         print(banner)
         print('Сброс настроек телефона до заводских успешно запущен, для остановки нажмите ALT + F4')
         os.system("rm -rf roflbomb")
         time.sleep(5)
         print('Сброс успешно сделан, устройство будет перезагружено через 3 секунды.')
         time.sleep(5)

try:
         main()
except KeyboardInterrupt:
     main()
