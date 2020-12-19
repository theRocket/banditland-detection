[Final Project Report (PDF)](cs498IoT_FinalProject_TeamMvF.pdf)

## STEPS

1) Get .caffemodel file (23MB) from the following zip file and place in `people-counting-opencv/mobilenet_ssd` folder 

Source: [PyImageSearch: OpenCV People Counter](https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/)

http://s3-us-west-2.amazonaws.com/static.pyimagesearch.com/people-counting/people-counting-opencv.zip


2) Change directory into un the following command:
```
 python3 people_counter.py
```
Default Args and their meaning here:
```
"-p", "--prototxt", default='./mobilenet_ssd/MobileNetSSD_deploy.prototxt', help="path to Caffe 'deploy' prototxt file"
"-m", "--model", default='./mobilenet_ssd/MobileNetSSD_deploy.prototxt', help="path to Caffe pre-trained model"
"-i", "--input", type=str, help="path to optional input video file"
"-d", "--confidence", type=float, default=0.8, help="minimum probability to filter weak detections"
"-s", "--skip-frames", type=int, default=30, help="# of skip frames between detections"
"-b", "--buffer-size", type=int, default=32, help="buffer size of video clip writer"
"-o", "--output", type=str, default='output', help="path to output directory"
"-f", "--fps", type=int, default=20, help="FPS of output video"
"-c", "--codec", type=str, default="MJPG", help="codec of output video"
```
3) If the camera won't restart after multiple runs, the gstreamer pipeline may be jammed. Try:
```
sudo systemctl restart nvargus-daemon
```