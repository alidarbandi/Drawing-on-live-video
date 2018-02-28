import numpy as np
import cv2

canvas=np.ones([300,400,3],'uint8')*0
cap=cv2.VideoCapture(0)

color=(0,205,226)
line_width=2
radius=5
point=(150,200)
pressed=False

def nothing(x):
    pass

conc = np.zeros((100,350,3), 'uint8')
cv2.namedWindow('Color controller')

# create trackbars for color change
cv2.createTrackbar('R','Color controller',0,255,nothing)
cv2.createTrackbar('G','Color controller',0,255,nothing)
cv2.createTrackbar('B','Color controller',0,255,nothing)
cv2.createTrackbar('Size','Color controller',1,20,nothing)



def click(event,x,y,flags,param):
	global point, pressed
	global canvas, pressed
	if event==cv2.EVENT_LBUTTONDOWN:
		pressed=True
		cv2.circle(canvas,(x,y),radius,color,-1)
		
		print("Pressed",x,y,flags,param)
	#	cv2.imshow('bcg',canvas)
		point=(x,y)
	elif event==cv2.EVENT_LBUTTONUP:
	    pressed=False
	elif event==cv2.EVENT_MOUSEMOVE and pressed==True:
		cv2.circle(canvas,(x,y),radius,color,-1)


cv2.namedWindow("frame")
cv2.setMouseCallback("frame",click)

while(True):
	ret, frame=cap.read()
	frame=cv2.resize(frame,(400,300))#,fx=1.0,fy=1.0)
	cv2.circle(frame,point,radius,color,line_width)
	final=cv2.add(frame,canvas)
	cv2.imshow('frame',final)

	# get current positions of 3 trackbars
	r = cv2.getTrackbarPos('R','Color controller')
	g = cv2.getTrackbarPos('G','Color controller')
	b = cv2.getTrackbarPos('B','Color controller')
	bs= cv2.getTrackbarPos('Size','Color controller')
	conc[:,:,0] = r
	conc[:,:,1]= g
	conc[:,:,2]=b
	color=(r,g,b)
	radius=bs
	cv2.imshow('Color controller',conc)
	ch=cv2.waitKey(1)
	if ch&0xFF==ord('c'):
		canvas=np.ones([300,400,3],'uint8')*0
	if ch&0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
