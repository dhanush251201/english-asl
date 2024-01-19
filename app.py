import cv2
import numpy as np

def Sequence(inp : list, action : str) -> None:
    for i in inp:
        param = i+".mov"
        playVideo(param,action)


def playVideo(inputFile:str, action : str) -> None:
    cap = cv2.VideoCapture(inputFile)
    if (cap.isOpened() == False):
        print("Error opening video stream or file")
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

Sequence(['vid1','vid1','vid1'],"hello i am Dhanush")