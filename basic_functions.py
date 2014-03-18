#Author: Lorin Vandegrift
#Description: These are the basic opencv functions that allow you to
#		read in and tranform images
#Date Created: 3/18/2014

import cv2
import cv

class Basic_Functions:
	frame = None
	cap = None
	#Opens the Video Stream from the default camera and reads first frame
	def __init__(self, camera = None):
		if camera is None:
			self.cap = cv2.VideoCapture(-1)
			flag, self.frame = self.cap.read()
		else:
			self.cap = cv2.VideoCapture(camera)
			flag, self.frame = self.cap.read()

	#Opens the Video Stream for the specified camera and reads first frame
	def get_next_frame(self):
		flag, self.frame = self.cap.read();
		
	#shows the captured video in the specified frame
	def show_frame(self, windowName = None, time = None):
		if windowName is None:
			cv2.imshow("window", self.frame)
		else:
			cv2.imshow(windowName, self.frame)
		if time is None:
			cv2.waitKey(0)
		else:
			cv2.waitKey(time)
	
	#write the current frame to the specified file
	def write_frame(self, filepath):
		cv2.imwrite(filepath, self.frame)
	
	#Convert the image to the specified constant. Constants:
	#Convert to Gray: cv.CV_BGR2GRAY
	#Convert to HSV: cv.CV_BGR2HSV
	#Convert to 
	def convert_image(self, convertion):
		self.frame = cv2.cvtColor(self.frame, convertion) 
