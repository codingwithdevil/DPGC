#
#    DPGC [Devil Proxy Grabber and checker ]   by Coding With Devil  https://www.youtube.com/c/CodingWithDevil/
#    This program comes with ABSOLUTELY NO WARRANTY
#    The use of the DPGC & its resources is COMPLETE RESPONSIBILITY of the END-USER.
#    Developers assume NO liability and are NOT responsible for any damage caused by this program.
#    Also we want to inform you that some of your actions may be ILLEGAL and you CAN NOT use this
#    software to test device, company or any other type of target without WRITTEN PERMISSION from them.
import sys
import subprocess as sp
import pkg_resources as pr
from time import sleep as wait

def rchecker():
    required = {'requests', 'bs4'}
    installed = {pkg.key for pkg in pr.working_set}
    mis = required - installed
    print("\033[1;34m checking Requirements : \n")
    wait(2)
    if mis:
        print("\033[1;31m %s Is Not installed \n"%(mis))
        wait(2)
        print(" ")
        print("\033[1;32m %s is Installing \n"%(mis))
        

        python = sys.executable
        sp.check_call([python, '-m', 'pip3', 'install', *mis], stdout=sp.DEVNULL)
    else:
        print("\033[1;32m Requirements Alredy Installed")