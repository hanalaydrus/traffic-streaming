import cv2
import threading
import time

class VideoCamera(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.video = cv2.VideoCapture('CarsDrivingUnderBridge.mp4')
        
    def run(self):
        while True:
            success, image = self.video.read()
            ret, jpeg = cv2.imencode('.jpg',image)
            self.frame = jpeg.tobytes()
            time.sleep(0.0001)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        return self.frame