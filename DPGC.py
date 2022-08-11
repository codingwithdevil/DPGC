#
#    DPGC [Devil Proxy Grabber and checker ]   by Coding With Devil  https://www.youtube.com/c/CodingWithDevil/
#    This program comes with ABSOLUTELY NO WARRANTY
#    The use of the DPGC & its resources is COMPLETE RESPONSIBILITY of the END-USER.
#    Developers assume NO liability and are NOT responsible for any damage caused by this program.
#    Also we want to inform you that some of your actions may be ILLEGAL and you CAN NOT use this
#    software to test device, company or any other type of target without WRITTEN PERMISSION from them.
import Defs.main.runner as runner
import Defs.theme.theme as theme
from time import sleep as wait
import Defs.rckr.rckr as rckr
if __name__ == "__main__":
    try :
        rckr.rchecker()
        wait(3)
        runner.runner()
    except KeyboardInterrupt :
        print(" ")
        print("\033[1;31m Exiting ..")
        wait(3)
    finally :
        print(theme.End_screenlogo)

