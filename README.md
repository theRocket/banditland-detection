Get .caffemodel file (23MB) from the following zip file and place in `people-counting-opencv/mobilenet_ssd` folder 

Source: [PyImageSearch: OpenCV People Counter](https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/)
http://s3-us-west-2.amazonaws.com/static.pyimagesearch.com/people-counting/people-counting-opencv.zip


Run the following command:
```
 python3 people-counting-opencv/people_counter.py -p people-counting-opencv/mobilenet_ssd/MobileNetSSD_deploy.prototxt -m people-counting-opencv/mobilenet_ssd/MobileNetSSD_deploy.caffemodel -d 0.7 -o output
```
Args:
```
"-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file"
"-m", "--model", required=True, help="path to Caffe pre-trained model"
"-i", "--input", type=str, help="path to optional input video file"
"-d", "--confidence", type=float, default=0.6, help="minimum probability to filter weak detections"
"-s", "--skip-frames", type=int, default=30, help="# of skip frames between detections"
"-b", "--buffer-size", type=int, default=32, help="buffer size of video clip writer"
"-o", "--output", type=str, required=True, help="path to output directory"
"-f", "--fps", type=int, default=20, help="FPS of output video"
"-c", "--codec", type=str, default="MJPG", help="codec of output video"
```