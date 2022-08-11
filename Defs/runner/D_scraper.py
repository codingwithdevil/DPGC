#
#    DPGC [Devil Proxy Grabber and checker ]   by Coding With Devil  https://www.youtube.com/c/CodingWithDevil/
#    This program comes with ABSOLUTELY NO WARRANTY
#    The use of the DPGC & its resources is COMPLETE RESPONSIBILITY of the END-USER.
#    Developers assume NO liability and are NOT responsible for any damage caused by this program.
#    Also we want to inform you that some of your actions may be ILLEGAL and you CAN NOT use this
#    software to test device, company or any other type of target without WRITTEN PERMISSION from them.
from time import sleep as wait
import requests as rqs
from bs4 import BeautifulSoup
import Defs.theme.theme as theme
from time import sleep
import Defs.main.runner as runner
import requests as rqs 
import threading
from requests import HTTPError
try:
    import Queue
except ImportError:
    import queue as Queue




def dscraper_http():
    print(" ")
    httplist = 'outputhttp.txt'
    print("\033[1;34m Cleaning File")
    open(httplist,'w').close()
    sleep(1)
    print(" ")
    print("\033[1;31m scraping http Proxy \n")
    
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=all&country=all"
   
    r = rqs.get(url)
    proxies = r.text
  

    with open(httplist, "a") as txt_file:
        if len(proxies) > 0:
                #print(line)
            txt_file.write(proxies)
    sleep(1)
    response = rqs.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=all&country=all")

    proxies = response.text
    with open(httplist, "a") as txt_file:
        txt_file.write(proxies)
    sleep(1)
    session = rqs.session()
    
    html = session.get("https://www.proxy-list.download/api/v1/get?type=http&anon=elite").text
    
    
    with open(httplist, "a") as txt_file:
        for line in html.split("\n"):
            if len(line) > 0:
                txt_file.write(line)

    sleep(1)
    
    page = rqs.get("http://us-proxy.org")
   
    
    soup = BeautifulSoup(page.text, "html.parser")

    proxies = set()
    table = soup.find("table", attrs={"class": "table table-striped table-bordered"})
    for row in table.findAll("tr"):
        count = 0
        proxy = ""
        for cell in row.findAll("td"):
            if count == 1:
                proxy += ":" + cell.text.replace("&nbsp;", "")
                proxies.add(proxy)
                break
            proxy += cell.text.replace("&nbsp;", "")
            count += 1

    with open(httplist, "a") as txt_file:
        for line in proxies:
            txt_file.write("".join(line) + "\n")
    print("\033[1;32m Proxy scraping finished ")
    sleep(2)
    print(" ")
    p_numb = len(open(httplist).readlines())
    print("\033[1;32m Current proxys in proxylist: %s\n" % (p_numb))

def dscraper_https():
    httpslist = 'output.txt'
    print(" ")
    print("\033[1;34m Cleaning File")
    open(httpslist,'w').close()
    sleep(2)
    print(" ")
    print("\033[1;31m scraping https Proxy \n")
    
    sr = rqs.get("https://spys.me/proxy.txt")
    res = sr.text

    
   
    r = rqs.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=all&country=all")
    proxies = r.text
  

    with open(httpslist, "a") as txt_file:
        if len(proxies) > 0:
                #print(line)
            txt_file.write(proxies)
    sleep(1)
    response = rqs.get("https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=all&country=all")

    proxies = response.text
    with open(httpslist, "a") as txt_file:
        txt_file.write(proxies)
    sleep(1)
    session = rqs.session()
    
    html = session.get("https://www.proxy-list.download/api/v1/get?type=https&anon=elite").text
    
    
    with open(httpslist, "a") as txt_file:
        for line in html.split("\n"):
            if len(line) > 0:
                txt_file.write(line)
    print("\033[1;32m Proxy scraping finished ")
    sleep(2)
    print(" ")
    p_numb = len(open(httpslist).readlines())
    print("\033[1;32m Current proxys in proxylist: %s\n" % (p_numb))

def dscraper_socks4():
    s4list = 'outputsocks4.txt'
    print(" ")
    print("\033[1;34m Cleaning File")
    open(s4list,'w').close()
    sleep(2)
    print(" ")
    print("\033[1;31m scraping socks4 Proxy \n")
    
     
   
    r = rqs.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=all&country=all")
    proxies = r.text
  

    with open(s4list, "a") as txt_file:
        if len(proxies) > 0:
                #print(line)
            txt_file.write(proxies)
    sleep(1)
    response = rqs.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=all&country=all")

    proxies = response.text
    with open(s4list, "a") as txt_file:
        txt_file.write(proxies)
    sleep(1)
    session = rqs.session()
    
    html = session.get("https://www.proxy-list.download/api/v1/get?type=socks4&anon=elite").text
    
    
    with open(s4list, "a") as txt_file:
        for line in html.split("\n"):
            if len(line) > 0:
                txt_file.write(line)
    print("\033[1;32m Proxy scraping finished ")
    sleep(2)
    print(" ")
    p_numb = len(open(s4list).readlines())
    print("\033[1;32m Current proxys in proxylist: %s\n" % (p_numb))

                
def dscraper_socks5():
    s5list = 'outputsocks5.txt'
    print(" ")
    print("\033[1;34m Cleaning File")
    open(s5list,'w').close()
    sleep(2)
    print(" ")
    print("\033[1;31m scraping socks5 Proxy \n")
    
    
   
    r = rqs.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=all&country=all")
    proxies = r.text
  

    with open(s5list, "a") as txt_file:
        if len(proxies) > 0:
                #print(line)
            txt_file.write(proxies)
    sleep(1)
    response = rqs.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=all&country=all")

    proxies = response.text
    with open(s5list, "a") as txt_file:
        txt_file.write(proxies)
    sleep(1)
    session = rqs.session()
    
    html = session.get("https://www.proxy-list.download/api/v1/get?type=socks5&anon=elite").text
    
    
    with open(s5list, "a") as txt_file:
        for line in html.split("\n"):
            if len(line) > 0:
                txt_file.write(line)
    print("\033[1;32m Proxy scraping finished ")
    print(" ")
    sleep(2)
    p_numb = len(open(s5list).readlines())
    print("\033[1;32m Current proxys in proxylist: %s\n" % (p_numb))


def dscraper_socks():
    slist = 'outputsocks.txt'
    print(" ")
    print("\033[1;34m Cleaning File")
    open(slist,'w').close()
    sleep(2)
    print(" ")
    print("\033[1;31m scraping socks [socks4,socks5] Proxy \n")
    
    
   
    r = rqs.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=all&country=all")
    proxies = r.text
  

    with open(slist, "a") as txt_file:
        if len(proxies) > 0:
                #print(line)
            txt_file.write(proxies)
    sleep(1)
    response = rqs.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=all&country=all")

    proxies = response.text
    with open(slist, "a") as txt_file:
        txt_file.write(proxies)
    sleep(1)
    session = rqs.session()
    
    html = session.get("https://www.proxy-list.download/api/v1/get?type=socks4&anon=elite").text
    
    
    with open(slist, "a") as txt_file:
        for line in html.split("\n"):
            if len(line) > 0:
                txt_file.write(line)
    sleep(1)
   
   
    r = rqs.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=all&country=all")
    proxies = r.text
  

    with open(slist, "a") as txt_file:
        if len(proxies) > 0:
                #print(line)
            txt_file.write(proxies)
    sleep(1)
    response = rqs.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=all&country=all")

    proxies = response.text
    with open(slist, "a") as txt_file:
        txt_file.write(proxies)
    sleep(1)
    session = rqs.session()
    
    html = session.get("https://www.proxy-list.download/api/v1/get?type=socks5&anon=elite").text
    
    
    with open(slist, "a") as txt_file:
        for line in html.split("\n"):
            if len(line) > 0:
                txt_file.write(line)
    print("\033[1;32m Proxy scraping finished ")
    sleep(2)
    print(" ")
    p_numb = len(open(slist).readlines())
    print("\033[1;32m Current proxys in proxylist: %s\n" % (p_numb))

def start_dscraper():
    
    print(theme.ds_logo)
    print(theme.dc1)
    i =input("\033[1;34m D-Scraper >>>")
    if i == "1":
        dscraper_http()
    elif i == "2":
        dscraper_https()
    elif i == "3":
        dscraper_socks4()
    elif i == "4":
        dscraper_socks5()
    elif i == "5":
        dscraper_socks()
    elif i == "6" :
        wait(3)
        runner.runner()
    else:
        print("\033[1;31m Please chose a valid option \n")

    sleep(3)
    print("\033[1;32m Do you want to check proxy y/n \n")
    opt =input("\033[1;34m D-Scraper >>>")
    print(" ")
    
    
    if opt == "y":
        global proxy_type
        if i == "1":
                

            proxy_type = "1"
            p = "outputhttp.txt"
            proxys = open(p).readlines()
            check_proxys(proxys)
            p_numb = len(open('working_proxy.txt').readlines())
            print("\033[1;32m Proxy Checking Finished \n")
            print("\033[1;32m Current proxys in proxylist: %s\n" % (p_numb))
            print("\033[1;32m Visit again")
            exit()
        elif i == "2":

                

            proxy_type = "2"
            p = "output.txt"
            proxys = open(p).readlines()
            check_proxys(proxys)
            p_numb = len(open('working_proxy.txt').readlines())
            print("\033[1;32m Proxy Checking Finished \n")
            print("\033[1;32m Current proxys in proxylist: %s\n" % (p_numb))
            print("\033[1;32m Visit again")
            exit()
        elif i == "3":
                

            proxy_type = "3"
            p = "outputsocks4.txt"
            proxys = open(p).readlines()
            check_proxys(proxys)
            p_numb = len(open('working_proxy.txt').readlines())
            print("\033[1;32m Proxy Checking Finished \n")
            print("\033[1;32m Current proxys in proxylist: %s\n" % (p_numb))
            print("\033[1;32m Visit again")
            exit()
        elif i == "4":
                

            proxy_type = "4"
            p = "outputsocks5.txt"
            proxys = open(p).readlines()
            check_proxys(proxys)
            p_numb = len(open('working_proxy.txt').readlines())
            print("\033[1;32m Proxy Checking Finished \n")
            print("\033[1;32m Current proxys in proxylist: %s\n" % (p_numb))
            print("\033[1;32m Visit again")
            exit()
            
        else:
            print("\033[1;31m Exiting ...... \n")
            exit()
    print("\033[1;34m Do you want to save in another name y/n")
    print(" ")
    i3 = input("\033[1;34m D-Scraper >>>")
    if i3 == "y":
        print("\033[1;31m Name of Text File :")
        i4 = input("\033[1;34m D-Scraper >>>")
        with open('working_proxy.txt','r') as firstfile, open(i4,'w') as secondfile:
            for line in firstfile:
                secondfile.write(line)

    else :
        print("\033[1;31m Exiting ... ")
        exit()
    
        
  

#checker


def check_proxy(q):
    
    
    
    if not q.empty():

        proxy = q.get(False)
        proxy = proxy.replace("\r", "").replace("\n", "")

        try:
            
           
            
            if proxy_type == "1" or "2" :

                pt  = {
                    'http': 'http://' + proxy,
                    'https': 'http://' + proxy  }
        
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
                print("\033[1;31m Exiting....\n ")
                sleep(5)

         

            
            
            url = 'https://api.ipify.org/'
            
            req = rqs.get(url, proxies=pt, timeout= 120)

            
            if req.ok :
                with open('working_proxy.txt' , 'a') as f:
                    f.writelines("".join(proxy) + "\n" )

                print( "\033[1;32m --[+] ", proxy, " | PASS \n" )
                
            else:
                
                print("\033[1;31m --[!] ", proxy, " | FAILED\n")
        except HTTPError as e :
            
            print("\033[1;31m %s Failed \n" %(proxy))
        except Exception as err:
            
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
        for workers in range(200):
            t = threading.Thread(target=check_proxy, args=(queue,))
            t.setDaemon(True)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        queuelock.release()  

