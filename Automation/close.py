import random
import pyautogui as ui
from DLG import closedlg
from NetHyTech_Pyttsx3_Speak import speak

closedlg_random = random.choice(closedlg)
def close():
    speak(closedlg_random,3)
    ui.hotkey("alt","f4")