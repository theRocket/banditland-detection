Get .caffemodel file (23MB) from the following zip file and place in `people-counting-opencv/mobilenet_ssd` folder 

```
http://s3-us-west-2.amazonaws.com/static.pyimagesearch.com/people-counting/people-counting-opencv.zip
```

Run the following command:
```
 python3 people-counting-opencv/people_counter.py -p people-counting-opencv/mobilenet_ssd/MobileNetSSD_deploy.prototxt -m people-counting-opencv/mobilenet_ssd/MobileNetSSD_deploy.caffemodel -d 0.7 -o output
```