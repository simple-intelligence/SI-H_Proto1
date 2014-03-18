#Author: Lorin Vandegrift
#Date Created: 3/18/2014
#Description: A simple sample program that continuously reads in images and displays them (video)

import cv2 

def sample2():
	cap = cv2.VideoCapture(0)
	while True:
		flag, img = cap.read()
		cv2.imshow("Window", img)
		if cv2.waitKey(25) >= 0:
			break;
	

if __name__ == '__main__':
	sample2()
