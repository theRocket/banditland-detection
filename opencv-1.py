import cv2
print(cv2.__version__)

# check gst-inspect-1.0 nvarguscamerasrc for property options
camSet='nvarguscamerasrc sensor-id=0 wbmode=2 tnr-mode=2 tnr-strength=1'
camSet+=' ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1, format=NV12'
camSet+=' ! nvvidconv flip-method=2 ! video/x-raw, width=800, height=600, format=BGRx'
camSet+=' ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)
while True:
    _, frame = cam.read()
    cv2.imshow('myCam',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
#.destroyAllWindows()