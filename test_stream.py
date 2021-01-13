import cv2
from time import ctime
import os

video = cv2.VideoCapture(r"rtsp://Atom:Atom1234@192.168.86.28/live", cv2.CAP_FFMPEG)


while True:

    ret,img = video.read()
    time = ctime()
        
    if '24:25:10' in time:
        with open('results.txt', 'a') as f:
            f.write("Stream completed succesfully program ended at {}".format(time))
        break

    try:

        if ret:
            cv2.imshow('FRAME', img)
        else:
            with open('log.txt', 'a') as log:
                t = ctime()
                log.write(f"Stream froze at {t}\n")
            break

        if (cv2.waitKey(1) & 0xFF == ord('q')) or not ret:
            breakcv2.de


    except KeyboardInterrupt:
        break

cap.release()
cv2.destroyAllWindows()

if '24:25:10' in time:
    with open('results.txt', 'a') as f:
        f.write("Stream completed succesfully program ended at {}".format(time))
else:
    os.system("python3 test_stream.py")