import cv2
import numpy as np
import PySimpleGUI as sg
from APICall import APICall
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# ---------------------------------------------------- #
# Gets input from the user
# ---------------------------------------------------- #

def getInput():
    layout = [
        [sg.Text("Enter String: "), sg.InputText(key='-INPUT-')],
        [sg.Button('Play Videos'), sg.Button('Exit')],]

    window = sg.Window('Video Player', layout, resizable=True)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            return -1
        elif event == 'Play Videos':
            return values['-INPUT-']



# ---------------------------------------------------- #
# Takes a list of actions as input for each action calls the playVideo function
# ---------------------------------------------------- #

def Sequence(inp : list, action : str) -> None:
    for i in inp:
        param = i+".mp4"
        playVideo(param,action)

# ---------------------------------------------------- #
# The logic to play the videos
# ---------------------------------------------------- #

def playVideo(inputFile:str, action : str) -> None:
    cap = cv2.VideoCapture("Videos/"+inputFile)
    if (cap.isOpened() == False):
        print(f"Error opening video stream or file {inputFile}")
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow(action, frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

# ---------------------------------------------------- #
# ENTRYPOINT
# ---------------------------------------------------- #

while True:
    INPUT = getInput()
    if INPUT == -1:
        break
    else:
        VIDEOS = APICall(INPUT)
        print(VIDEOS)
        Sequence(VIDEOS, INPUT)

# INPUT1 = "I am thirsty, give me hot water"

# print( APICall(INPUT1) )
# Sequence(['me','muscle','murder'],"hello i am Dhanush")

# print( getInput() )
