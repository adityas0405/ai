import os
import keyboard
import pyautogui
import webbrowser   
from time import sleep

def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "search" in Query:
        Nameofweb = Query.replace("search ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    
    elif "google" in Query:
        Nameofweb = Query.replace("google ","")
        Link = f"https://www.google.com/search?q={Nameofweb}"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameoftheapp = Query.replace("launch ","")
        #pyautogui.press('win + space')
        keyboard.press_and_release('win + space')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True

    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        #pyautogui.press('win + space')
        keyboard.press_and_release('win + space')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True

    elif "start" in Query:
        Nameoftheapp = Query.replace("start ","")
        #pyautogui.press('win')
        keyboard.press_and_release('win + space')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True

