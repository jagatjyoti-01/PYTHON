#robo reader(project name)


# import os
# if __name__=='__main__':
#     print("wellcome to my python 1st project creted by jyoti")
#     x=input("enter you want to speak: ")
#     command=f"say {x}"
#     os.system(command)
import win32com.client

if __name__ == '__main__':
    print("Welcome to my Python 1st project created by Jyoti")
    x = input("Enter what you want to speak: ")

    # Initialize the text-to-speech engine
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    # Speak the user input
    speaker.Speak(x)


