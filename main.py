# importing all required function from another folder
from JARVIS_AI_LISTENING_FUNCTION.listen import listen
from JARVIS_AI_SPEAK_FUNCTION.speak import speak



def main():
    while True:
        x = listen().lower()
        if "hello" in x :
            speak("hello sir")
        else:
            pass


main()