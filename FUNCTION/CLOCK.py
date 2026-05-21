import datetime
from NetHyTech_TTS import *



def what_is_the_time():
    try:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        Speak(f"The time is {current_time}")

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        Speak(error_message)

