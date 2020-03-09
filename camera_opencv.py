import os
from cv2 import cv2 
from base_camera import BaseCamera
from datetime import datetime

class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(0)
            
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = 0

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            cv2.putText(img,str(datetime.now().strftime(
                "%b %d %Y %H:%M:%S")),(10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,170,250),2,cv2.LINE_AA)            
            yield cv2.imencode('.jpg', img)[1].tobytes()
