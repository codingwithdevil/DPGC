#
#    DPGC [Devil Proxy Grabber and checker ]   by Coding With Devil  https://www.youtube.com/c/CodingWithDevil/
#    This program comes with ABSOLUTELY NO WARRANTY
#    The use of the DPGC & its resources is COMPLETE RESPONSIBILITY of the END-USER.
#    Developers assume NO liability and are NOT responsible for any damage caused by this program.
#    Also we want to inform you that some of your actions may be ILLEGAL and you CAN NOT use this
#    software to test device, company or any other type of target without WRITTEN PERMISSION from them.

import Defs.theme.theme as theme
import Defs.runner.D_scraper as scraper
import Defs.runner.D_checker as checker
from time import sleep as wait
from subprocess import call as run 

def runner():
        
        run("clear")
        print(theme.d_sg)
        wait(2)
        print(theme.d_sg1)
        i = input("\033[1;32m DPGC>>> \033[1;34m ")
        if i == "1":
            run("clear")
            wait(3)
            scraper.start_dscraper()
        elif i == "2":
            run("clear")
            wait(3)
            checker.start_dchecker()

        elif i == "3":
            print(theme.about)
            i2 = input("\033[1;32m DPGC>>> \033[1;34m ")
            if i2 == "y":
                run("clear")
                runner()
            else :
                print("\033[1;31m Exiting...")
                exit()
        elif i == "4":
            print(" ")
            print("\033[1;31m Exiting ..")
            wait(3)
        else:
            print("\033[1;31m Invalid Option \n")
            print("")
            wait(3)
            runner()
            
            
    
    
    