#################################
#                               #
#       Created By Costi        #
#                               #
#################################
import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import datetime as dt 
# import math
import copy

PlayBackFPS = 30.0
CaptureFPS  = 1
FramesPast = 0
FrameMaximum = 0
FileName = 'Video {}.avi'.format(dt.datetime.now().strftime('%Y %m %d %H %M %S'))

Capture = cv2.VideoCapture(1)

Video = VideoWriter(FileName, VideoWriter_fourcc('F','M','P','4'), PlayBackFPS, (int(Capture.get(3)), int(Capture.get(4))) )

while True:
    RetVal, Frame = Capture.read()
    
    Frame = cv2.rotate(Frame, cv2.cv2.ROTATE_180)

    UIFrame = copy.copy(Frame)
    UIFrame = cv2.putText(UIFrame, str(FramesPast), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 10, 0), 2, cv2.LINE_AA)
    UIFrame = cv2.putText(UIFrame, str(CaptureFPS), (50, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 215, 255), 2, cv2.LINE_AA)

    if RetVal:
        cv2.imshow('Capture', UIFrame)
        if FrameMaximum == 0 or FramesPast < FrameMaximum:
            FramesPast += 1
            Video.write(Frame)
        else: print('Time Lapse Finished!'); break

    if cv2.waitKey(round(1000 / CaptureFPS)) & 0xFF == 27: break

cv2.destroyAllWindows()
Capture.release()
Video.release()