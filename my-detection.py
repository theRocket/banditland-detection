#!/usr/bin/python3

import jetson.inference
import jetson.utils
import boto3

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("csi://0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file

# Create an SNS client
sns = boto3.client('sns',region_name='us-west-2')

while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img)
	for detection in detections:
		#print(detection.ClassID, detection.Confidence)
		if ((detection.ClassID==1) & (detection.Confidence>=0.90)):
			# Publish a simple message to the specified SNS topic
			response = sns.publish(
				TopicArn='arn:aws:sns:us-west-2:876612415673:xavier_securitycam',    
				Message='Confidence: '+str(detection.Confidence),    
			)
			print(response)
			break

	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
