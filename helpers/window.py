import PySimpleGUI as sg
import cv2
import os

def play_videos(video_files):
    for video_file in video_files:
        cap = cv2.VideoCapture(video_file)
        if not cap.isOpened():
            sg.popup_error(f"Error opening video file: {video_file}")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow('Video Player', frame)

            if cv2.waitKey(30) & 0xFF == 27:
                break

        cap.release()

    cv2.destroyAllWindows()


def main():
    layout = [
        [sg.Text("Enter String: "), sg.InputText(key='-INPUT-')],
        [sg.Button('Play Videos'), sg.Button('Exit')],]

    window = sg.Window('Video Player', layout, resizable=True)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Play Videos':
            input_string = values['-INPUT-']

            video_files = [f for f in os.listdir('videos') if f.startswith('output') and f.endswith('.mov')]
            VIDEOS = []


            if not video_files:
                sg.popup_error("No video files found.")
            else:
                play_videos([os.path.join('videos', file) for file in video_files])

if __name__ == '__main__':
    main()
