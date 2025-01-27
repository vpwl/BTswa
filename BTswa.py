#//     TODO Add more stuff 
from siem import siem
import time
import os
import sys
Banner = """
############          Blue Team swiss army knife       ############
############           --for Blue teamers--            ############
############        https://github.com/Richycam        ############
"""

art1 = """
 ___________________
 | _______________ |
 | |    BTswa    | |
 | |             | |
 | |x           x| |
 | |             | |
 | |             | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []| 
L___________________J 

"""
art2 = """
 ___________________
 | _______________ |
 | |    BTswa    | |
 | |             | |
 | |x x   x   x x| |
 | |             | |
 | |             | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []| 
L___________________J 

"""

art3 = """
 ___________________
 | _______________ |
 | |    BTswa    | |
 | |             | |
 | |  RichyCam   | |
 | |             | |
 | |             | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []| 
L___________________J 

"""
art4 = """
 ___________________
 | _______________ |
 | |    BTswa    | |
 | |             | |
 | |  RichyCam   | |
 | |             | |
 | | Github.com  | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []|
L___________________J    
   
"""




def clear():
    os.system("clear")
    os.system("cls")

def for_art():
    list = [art1, art2, art3, art4]
    for art in list:
        print(art)
        time.sleep(0.7)
        clear()

def exit():
    sys.exit()




def menu():

    print("--------------------------------------------")
    print(siem.get_tool())    
    print("1) siem link ")
    print("2) siem documents")
    print("3) Nmap")
    print("4) ")
    print("--------------------------------------------")


def main():
    menu()
    main_cntrl = input("choose usage \n")
    match main_cntrl:
        case "1":
            clear()
            print(siem.get_tool())
            back = input("go back? Y/N? \n ").lower
            if back == "y":
                clear()
                print(Banner)
                main()

        case "2":
            docs = siem.get_tool()
            if docs == "kibana" or docs == "elastic": 
                    print("https://www.elastic.co/guide/index.html?utm_campaign=Google-B-EMEA-UKI-Exact&utm_content=Brand-Core-Documentation&utm_source=google&utm_medium=cpc&device=c&utm_term=elastic%20documentation&gad_source=1&gclid=EAIaIQobChMIsuHa15OuiAMV6JtQBh2tHgypEAAYASAAEgKobvD_BwE") 
                    back = input("go back? Y/N?")
                    if back == "y":
                        clear()
                        print(Banner)
                        main()
            elif docs == "splunk":
                    print("https://docs.splunk.com/Documentation") 
                    back = input("go back? Y/N?").lower()
                    if back == "y":
                        clear()
                        print(Banner)
                        main()
            elif docs == "velociraptor":
                print("https://docs.velociraptor.app/docs/")


        case "3":
            clear()
            ip = input("ip to scan \n")
            print("scan type") 
            print("1) simple scan")
            print("2) version detector")
            scan_type = input("")
            match scan_type:
                case "1":
                    clear()
                    simple_scan = "nmap {0}".format(ip)
                    os.system(simple_scan)
                    back = input("want to go back? Y/N? \n").lower()
                    if back == "Y":
                        clear()
                        print(Banner)
                        main()
                case "2":
                    clear()
                    ver_scan = "nmap {0} -A".format(ip)
                    os.system(ver_scan)
                    back = input("want to go back Y/N? \n")
                    if back == "Y":
                        clear()
                        print(Banner)
                        main()                            

        case "4":
            #//     TODO Add to this 
            clear()


clear()
for_art()
tool = input(str("tool name? \n")).lower()
link = input("tool link? \n").lower()
siem = siem(tool,link)
clear()
print(Banner)
main()

