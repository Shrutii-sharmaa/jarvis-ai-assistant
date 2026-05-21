from NetHyTech_STT import listen
from NetHyTech_Pyttsx3_Speak import speak
from brain import Query_brain
import threading
from os import getcwd

bye_key_word = ["bye", "goodbye"]

# Variable to track if the bye command has been given
exit_flag = False


def clear_input_file():
    with open(f"{getcwd()}\\input.txt", "w") as input_file:
        input_file.truncate(0) 
        
def Check():
    global exit_flag
    output_text = ""
    while not exit_flag:
        try:
            with open("input.txt", "r") as input_text:
                current_text = input_text.read().lower()  # Convert to lowercase for consistency
            if current_text != output_text:
                output_text = current_text
                wake_cmd = output_text.strip()  # Remove leading/trailing whitespaces
                Query_brain(wake_cmd)
                # Check if any of the bye keywords are in the wake command
                if any(keyword in wake_cmd for keyword in bye_key_word):
                    exit_flag = True
        except Exception as e:
            print("Error:", e)

def main():
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=Check)
    t1.start()
    t2.start()
    t1.join()  # Waits for the listen thread to finish
    t2.join()  # Waits for the Check thread to finish

if __name__ == "__main__":
    clear_input_file()
    main()
