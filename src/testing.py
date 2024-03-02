import cv2
import numpy as np
import PySimpleGUI as sg
import json
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

def getInput() -> list:
    FILE = open("testing/test.txt")
    SENTENCES = []
    for i in FILE.readlines():
        SENTENCES.append(i[:-1])
    return(SENTENCES)

# ---------------------------------------------------------- #
# Takes a list of actions as input
# For each action calls the playVideo function
# ---------------------------------------------------------- #

def Sequence(inputString : list, action : str) -> list:
    TOKENS = []
    for i in inputString:
        TOKENS.append(i.lower()+".mp4")
    return TOKENS

# ---------------------------------------------------------- #
# The logic to play the videos
# ---------------------------------------------------------- #

def testTokensBefore(inputFile : str, action : str) -> None:
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


def findTokensBefore(SEQUENCE : list, action : str) -> dict:
    result = {
        'name': action,
        'tokenCount':len(SEQUENCE),
        'found' : [],
        'missing' : [],
        'SimilarityFound':[],
        'SimilarityMissing':[]
    }
    for i in SEQUENCE:
        try:
            with open(f"Videos/{i}") as f:
                result["found"].append(i)
        except:
            result["missing"].append(i)
            # SIM = similaritySearch(i)
            # # Returns [TOKEN, SCORE, INDEX]
            # if SIM[1] > 0.5:
            #     result["SimilarityFound"].append(SIM[0])
            # else:
            #     result["SimilarityMissing"].append(SIM[0])
    return result


def findTokensAfter(SEQUENCE : list, action : str) -> dict:
    result = {
        'name': action,
        'tokenCount':len(SEQUENCE),
        'found' : [],
        'missing' : [],
        'SimilarityFound':[],
        'SimilarityMissing':[]
    }
    for i in SEQUENCE:
        try:
            with open(f"Videos/{i}") as f:
                result["found"].append(i)
        except:
            result["missing"].append(i)
            SIM = similaritySearch(i[:-4])
            # Returns [TOKEN, SCORE, INDEX]
            if SIM[1] > 0.5:
                result["SimilarityFound"].append(SIM[0])
            else:
                result["SimilarityMissing"].append(SIM[0])
    return result
# ---------------------------------------------------------- #
# ENTRYPOINT
# ---------------------------------------------------------- #
# def main():
#     while True:
#         INPUT = getInput()
#         if INPUT == 'ERR':
#             break
#         else:
#             VIDEOS = APICall(INPUT)
#             print(VIDEOS)
#             Sequence(VIDEOS, INPUT)

def main():
    RESULTSBEFORE = []
    RESULTSAFTER = []
    for i in getInput():
        VIDEO = APICall(i)
        SEQUENCE = Sequence(VIDEO,i)
        RESULTSBEFORE.append(findTokensBefore(SEQUENCE,i))
        RESULTSAFTER.append(findTokensAfter(SEQUENCE,i))
    print(json.dumps(RESULTSBEFORE, indent=4))
    f1 = open('resultsbefore.json', 'w')
    f2 = open('resultsafter.json', 'w')
    f1.write(json.dumps(RESULTSBEFORE,indent=4))
    f2.write(json.dumps(RESULTSAFTER,indent=4))
if __name__ == "__main__":
    main()
