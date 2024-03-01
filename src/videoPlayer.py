import cv2
import numpy as np
import PySimpleGUI as sg
from APICall import APICall
from openai import OpenAI
from similarity import similaritySearch

# ---------------------------------------------------------- #
# Connection to the LLM server
# ---------------------------------------------------------- #

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# ---------------------------------------------------------- #
# Gets input from the user
# ---------------------------------------------------------- #

def getInput() -> str:
    layout = [
        [sg.Text("Enter String: "), sg.InputText(key='-INPUT-')],
        [sg.Button('Play Videos'), sg.Button('Exit')],]

    window = sg.Window('Video Player', layout, resizable=True)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            return 'ERR'
        elif event == 'Play Videos':
            return values['-INPUT-']

# ---------------------------------------------------------- #
# Takes a list of actions as input
# For each action calls the playVideo function
# ---------------------------------------------------------- #

def Sequence(inp : list, action : str) -> None:
    for i in inp:
        param = i.lower()+".mp4"
        playVideo(param,action)

# ---------------------------------------------------------- #
# The logic to play the videos
# ---------------------------------------------------------- #

def playVideo(inputFile : str, action : str) -> None:
    cap = cv2.VideoCapture("Videos/"+inputFile)
    if (cap.isOpened() == False):
        print(f"Error opening video stream or file {inputFile}") # EDIT THIS
        print(f"calling similaritySearch with {inputFile[:-4]}")
        tempCap = similaritySearch(inputFile[:-4])
        print(tempCap,inputFile)
        if tempCap[1]>0.5:
            print(f"FOUND Similar video to {inputFile}, {tempCap[0]} with confidence {tempCap[1]}")
            cap = cv2.VideoCapture("Videos/"+tempCap[0]+".mp4")
        else:
            print(f"No replacement found")

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

# ---------------------------------------------------------- #
# ENTRYPOINT
# ---------------------------------------------------------- #
def main():
    while True:
        INPUT = getInput()
        if INPUT == 'ERR':
            break
        else:
            VIDEOS = APICall(INPUT)
            print(VIDEOS)
            Sequence(VIDEOS, INPUT)

if __name__ == "__main__":
    main()
