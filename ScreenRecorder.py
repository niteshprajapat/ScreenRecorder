import cv2           # pip install opencv-python
import numpy as np
from PIL import ImageGrab

def screenrecorder():
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter("output.avi",fourcc,5.0,(1366,768))
    
    while True:
        img=ImageGrab.grab()
        imp_np=np.array(img)
        frame=cv2.cvtColor(imp_np,cv2.COLOR_BGR2RGB)
        cv2.imshow("screen recorder",frame)
        out.write(frame)
        
        if cv2.waitKey(1) ==27:
            break
            
    out.release()
    cv2.destroyAllWindows()
    
screenrecorder()
