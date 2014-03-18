#Author: Lorin Vandegrift
#Date Created: 3/18/2014
#Description: A simple sample program that reads in an image then displays it

import cv2 

def sample1():
	cap = cv2.VideoCapture(0)
	flag, img = cap.read()
	cv2.imshow("Window", img)
	cv2.waitKey(0)


if __name__ == '__main__':
	sample1()
