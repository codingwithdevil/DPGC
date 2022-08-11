#
#    DPGC [Devil Proxy Grabber and checker ]   by Coding With Devil  https://www.youtube.com/c/CodingWithDevil/
#    This program comes with ABSOLUTELY NO WARRANTY
#    The use of the DPGC & its resources is COMPLETE RESPONSIBILITY of the END-USER.
#    Developers assume NO liability and are NOT responsible for any damage caused by this program.
#    Also we want to inform you that some of your actions may be ILLEGAL and you CAN NOT use this
#    software to test device, company or any other type of target without WRITTEN PERMISSION from them.


pallet =[
  '\033[91m',
  '\033[92m',
  '\033[94m',


] 


ds_logo = (""" \033[1;32m                                                                                                                                                                          
            DDDDDDDDDDDDD                            SSSSSSSSSSSSSSS                                                                                                                    
            D::::::::::::DDD                       SS:::::::::::::::S                                                                                                                   
            D:::::::::::::::DD                    S:::::SSSSSS::::::S                                                                                                                   
            DDD:::::DDDDD:::::D                   S:::::S     SSSSSSS                                                                                                                   
                D:::::D    D:::::D                  S:::::S                ccccccccccccccccrrrrr   rrrrrrrrr   aaaaaaaaaaaaa  ppppp   ppppppppp       eeeeeeeeeeee    rrrrr   rrrrrrrrr   
                D:::::D     D:::::D                 S:::::S              cc:::::::::::::::cr::::rrr:::::::::r  a::::::::::::a p::::ppp:::::::::p    ee::::::::::::ee  r::::rrr:::::::::r  
                D:::::D     D:::::D                  S::::SSSS          c:::::::::::::::::cr:::::::::::::::::r aaaaaaaaa:::::ap:::::::::::::::::p  e::::::eeeee:::::eer:::::::::::::::::r 
                D:::::D     D:::::D ---------------   SS::::::SSSSS    c:::::::cccccc:::::crr::::::rrrrr::::::r         a::::app::::::ppppp::::::pe::::::e     e:::::err::::::rrrrr::::::r
                D:::::D     D:::::D -:::::::::::::-     SSS::::::::SS  c::::::c     ccccccc r:::::r     r:::::r  aaaaaaa:::::a p:::::p     p:::::pe:::::::eeeee::::::e r:::::r     r:::::r
                D:::::D     D:::::D ---------------        SSSSSS::::S c:::::c              r:::::r     rrrrrrraa::::::::::::a p:::::p     p:::::pe:::::::::::::::::e  r:::::r     rrrrrrr
                D:::::D     D:::::D                             S:::::Sc:::::c              r:::::r           a::::aaaa::::::a p:::::p     p:::::pe::::::eeeeeeeeeee   r:::::r            
                D:::::D    D:::::D                              S:::::Sc::::::c     ccccccc r:::::r          a::::a    a:::::a p:::::p    p::::::pe:::::::e            r:::::r            
            DDD:::::DDDDD:::::D                   SSSSSSS     S:::::Sc:::::::cccccc:::::c r:::::r          a::::a    a:::::a p:::::ppppp:::::::pe::::::::e           r:::::r            
            D:::::::::::::::DD                    S::::::SSSSSS:::::S c:::::::::::::::::c r:::::r          a:::::aaaa::::::a p::::::::::::::::p  e::::::::eeeeeeee   r:::::r            
            D::::::::::::DDD                      S:::::::::::::::SS   cc:::::::::::::::c r:::::r           a::::::::::aa:::ap::::::::::::::pp    ee:::::::::::::e   r:::::r            
            DDDDDDDDDDDDD                          SSSSSSSSSSSSSSS       cccccccccccccccc rrrrrrr            aaaaaaaaaa  aaaap::::::pppppppp        eeeeeeeeeeeeee   rrrrrrr            
                                                                                                                             p:::::p                                                    
                                                                                                                             p:::::p                                                    
                                                                                                                             p:::::::p                                                   
                                                                                                                             p:::::::p                                                   
                                                                                                                             p:::::::p                                                   
                                                                                                                             ppppppppp                                                   
  
  
                                                                                                                                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ \n
                                                                                                                       \033[1;31m         |C|o|d|e|d|b|y|C|o|d|i|n|g|W|i|t|h|D|e|v|i|l|\n
                                                                                                                   \033[1;32m             +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+             
                                                                                                                                                          \n """) 


dc_logo = ("""\033[1;32m
                                                                                                                                                                               
DDDDDDDDDDDDD                                 CCCCCCCCCCCCChhhhhhh                                                     kkkkkkkk                                                
D::::::::::::DDD                           CCC::::::::::::Ch:::::h                                                     k::::::k                                                
D:::::::::::::::DD                       CC:::::::::::::::Ch:::::h                                                     k::::::k                                                
DDD:::::DDDDD:::::D                     C:::::CCCCCCCC::::Ch:::::h                                                     k::::::k                                                
  D:::::D    D:::::D                   C:::::C       CCCCCC h::::h hhhhh           eeeeeeeeeeee        cccccccccccccccc k:::::k    kkkkkkk eeeeeeeeeeee    rrrrr   rrrrrrrrr   
  D:::::D     D:::::D                 C:::::C               h::::hh:::::hhh      ee::::::::::::ee    cc:::::::::::::::c k:::::k   k:::::kee::::::::::::ee  r::::rrr:::::::::r  
  D:::::D     D:::::D                 C:::::C               h::::::::::::::hh   e::::::eeeee:::::ee c:::::::::::::::::c k:::::k  k:::::ke::::::eeeee:::::eer:::::::::::::::::r 
  D:::::D     D:::::D --------------- C:::::C               h:::::::hhh::::::h e::::::e     e:::::ec:::::::cccccc:::::c k:::::k k:::::ke::::::e     e:::::err::::::rrrrr::::::r
  D:::::D     D:::::D -:::::::::::::- C:::::C               h::::::h   h::::::he:::::::eeeee::::::ec::::::c     ccccccc k::::::k:::::k e:::::::eeeee::::::e r:::::r     r:::::r
  D:::::D     D:::::D --------------- C:::::C               h:::::h     h:::::he:::::::::::::::::e c:::::c              k:::::::::::k  e:::::::::::::::::e  r:::::r     rrrrrrr
  D:::::D     D:::::D                 C:::::C               h:::::h     h:::::he::::::eeeeeeeeeee  c:::::c              k:::::::::::k  e::::::eeeeeeeeeee   r:::::r            
  D:::::D    D:::::D                   C:::::C       CCCCCC h:::::h     h:::::he:::::::e           c::::::c     ccccccc k::::::k:::::k e:::::::e            r:::::r            
DDD:::::DDDDD:::::D                     C:::::CCCCCCCC::::C h:::::h     h:::::he::::::::e          c:::::::cccccc:::::ck::::::k k:::::ke::::::::e           r:::::r            
D:::::::::::::::DD                       CC:::::::::::::::C h:::::h     h:::::h e::::::::eeeeeeee   c:::::::::::::::::ck::::::k  k:::::ke::::::::eeeeeeee   r:::::r            
D::::::::::::DDD                           CCC::::::::::::C h:::::h     h:::::h  ee:::::::::::::e    cc:::::::::::::::ck::::::k   k:::::kee:::::::::::::e   r:::::r            
DDDDDDDDDDDDD                                 CCCCCCCCCCCCC hhhhhhh     hhhhhhh    eeeeeeeeeeeeee      cccccccccccccccckkkkkkkk    kkkkkkk eeeeeeeeeeeeee   rrrrrrr            


                                                                                                                               +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ \n
                                                                                                                       \033[1;31m        |C|o|d|e|d|b|y|C|o|d|i|n|g|W|i|t|h|D|e|v|i|l|\n
                                                                                                                   \033[1;32m            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+             
                                                                                                                                                          \n """)                                                                                                                                                                               


d_sg ="""



{0}d8888b. d88888b db    db d888888b db      {1}d8888b. d8888b.  .d88b.  db    db db    db  d888b  d8888b.  .d8b.  d8888b. d8888b. d88888b d8888b.         .o88b. db   db d88888b  .o88b. db   dD d88888b d8888b. 
{0}88  `8D 88'     88    88   `88'   88      {1}88  `8D 88  `8D .8P  Y8. `8b  d8' `8b  d8' 88' Y8b 88  `8D d8' `8b 88  `8D 88  `8D 88'     88  `8D        d8P  Y8 88   88 88'     d8P  Y8 88 ,8P' 88'     88  `8D 
{0}88   88 88ooooo Y8    8P    88    88      {1}88oodD' 88oobY' 88    88  `8bd8'   `8bd8'  88      88oobY' 88ooo88 88oooY' 88oooY' 88ooooo 88oobY'        8P      88ooo88 88ooooo 8P      88,8P   88ooooo 88oobY' 
{0}88   88 88~~~~~ `8b  d8'    88    88      {1}88~~~   88`8b   88    88  .dPYb.     88    88  ooo 88`8b   88~~~88 88~~~b. 88~~~b. 88~~~~~ 88`8b  {2} C8888D{1} 8b      88~~~88 88~~~~~ 8b      88`8b   88~~~~~ 88`8b   
{0}88  .8D 88.      `8bd8'    .88.   88booo. {1}88      88 `88. `8b  d8' .8P  Y8.    88    88. ~8~ 88 `88. 88   88 88   8D 88   8D 88.     88 `88.        Y8b  d8 88   88 88.     Y8b  d8 88 `88. 88.     88 `88. 
{0}Y8888D' Y88888P    YP    Y888888P Y88888P {1}88      88   YD  `Y88P'  YP    YP    YP     Y888P  88   YD YP   YP Y8888P' Y8888P' Y88888P 88   YD         `Y88P' YP   YP Y88888P  `Y88P' YP   YD Y88888P 88   YD 
                                                                                                                                                                                                            
                                                                                                                                                                            \033[1;31m Coded By coding With Devil                                                                                
                                                                                                                                                                                                            
""".format(pallet[0],pallet[1],pallet[2])

d_sg1 ="""
{0}Options :

    {1}[1] Proxy Grabber

    {1}[2] Proxy Checker

    {1}[3] About

    {1}[4] Exit
 
""".format(pallet[1],pallet[0])

End_screenlogo = """ 
                                                  \033[1;31m  Coded By  :   Coding With devil  \n

                                                      \033[1;37m       Follow Me    \n

                                                            \033[1;37m    on       \n   
                                                                                             

                                             \033[1;35m       Instagram :    codingwithdevil  \n  
                                                                                             

                                            \033[1;33m        Youtube   :    Coding With Devil \n
                                                                                        


                                                       \033[5;31m    Vist Again \n   """   


about = """
{1}About :-  
      \033[1;31m  Coded By  :   Coding With devil  \n

{1}Saving location :

    {0}  http = outpythttp.txt

    {0}  https = output.txt

    {0}  socks4 = outputsocks4.txt

    {0}  socks4 = outputsocks4.txt

    {0}  socks5 = outputsocks.txt

    {0}  socks = outputsocks.txt [socks4,socks5]

Do You want to go back to main menu y/n:

""".format(pallet[1],pallet[2])

dc = """
{0}proxy type: 

        {1}[1] http

        {1}[2] https

        {1}[3] socks4

        {1}[4] socks5 
        
        {0}[5] Return 
        
  """.format(pallet[0],pallet[1])


dc1 = """
{0}proxy type: 

        {1}[1] http

        {1}[2] https

        {1}[3] socks4

        {1}[4] socks5 
        
        {1}[5] socks[4,5]

        {0}[6] Return 
        
  """.format(pallet[0],pallet[1])

