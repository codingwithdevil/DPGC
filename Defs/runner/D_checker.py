#
#    DPGC [Devil Proxy Grabber and checker ]   by Coding With Devil  https://www.youtube.com/c/CodingWithDevil/
#    This program comes with ABSOLUTELY NO WARRANTY
#    The use of the DPGC & its resources is COMPLETE RESPONSIBILITY of the END-USER.
#    Developers assume NO liability and are NOT responsible for any damage caused by this program.
#    Also we want to inform you that some of your actions may be ILLEGAL and you CAN NOT use this
#    software to test device, company or any other type of target without WRITTEN PERMISSION from them.
import requests as rqs 
import threading
from requests import HTTPError
import queue as Queue
import Defs.theme.theme as theme
from time import sleep as wait
from subprocess import call as run_command
import Defs.main.runner as runner

def check_proxy(q):
    
    
    
    if not q.empty():

        proxy = q.get(False)
        proxy = proxy.replace("\r", "").replace("\n", "")

        try:
            
            global pt
            
            if proxy_type == "1" or "2":

                pt  = {
                    'http': 'http://' + proxy,
                    'https': 'http://' + proxy}
        
            
        
            elif proxy_type == "3" :

                pt = {
                    'http' : 'socks4://' + proxy,
                    'https' : 'socks4://' + proxy}
        
            elif proxy_type == "4":

                pt = {
                    'http' : 'socks5://' + proxy,
                    'https' : 'socks5://' + proxy }
        
            else :
                print("invalid option continuing with default")
                wait(5)
                start_dchecker()

         

            
            
            url = 'https://api.ipify.org/'
            
            req = rqs.get(url, proxies=pt, timeout= 120)

            if req.ok :
                with open(p , 'a') as f:
                    f.writelines("".join(proxy) + "\n" )

                
               
                print( "\033[1;32m --[+] ", proxy, " | PASS \n" )
                
            else:
                
                print("\033[1;31m --[!] ", proxy, " | FAILED\n")
        except HTTPError as e :
            
            print("\033[1;31m %s Failed \n" %(proxy))
        except Exception as err:
            #print(req.status_code)
            print("\033[1;31m --[!] %s  | FAILED \n" %(proxy))
            
            pass
            return
def check_proxys(proxys):
    
    
    
    queue = Queue.Queue()
    queuelock = threading.Lock()
    threads = []

    for proxy in proxys:
        queue.put(proxy)

    while not queue.empty():
        queuelock.acquire()
        for workers in range(100):
            t = threading.Thread(target=check_proxy, args=(queue,))
            t.setDaemon(True)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        queuelock.release()  


def start_dchecker():

   
        global proxy_type
        global p
        run_command("clear")
        print(theme.dc_logo)
        open('working_proxy.txt', 'w').close()
        print(theme.dc)
        proxy_type = input("\033[1;34m D-Checker >>> \033[1;34m ")
        print(" ")
        
        if proxy_type == "5":
            wait(3)
            runner.runner()
        p = input("\033[1;34m proxy list path:-")
        proxys = open(p).readlines()
        open(p, "w").close()
        check_proxys(proxys)
        p_numb = len(open('working_proxy.txt').readlines())
        print("\033[1;32m Proxy Checking Finished \n")
        print("\033[1;32m Current proxys in proxylist: %s\n" % (p_numb))
   