from PIL import ImageGrab
import numpy   as np 
import cv2
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
capture_video = cv2.VideoWriter('output.mp4',fourcc,30.0,(width,height))


while True:
    img = ImageGrab.grab(bbox=(0,0,1280,720))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('cature',img_final)
    capture_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break
