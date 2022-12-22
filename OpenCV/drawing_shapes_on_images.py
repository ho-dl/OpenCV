import cv2

image=cv2.imread("demo.jpg",1)
cv2.circle(image,(200,200),100,(0,0,255),-1) #circle_on_image_( -1 is for filling circle with color )
cv2.rectangle(image,(0,0),(400,400),(0,255,0),4) #rectangle_on_image
font=cv2.FONT_HERSHEY_COMPLEX #FONT
cv2.putText(image,"hello",(100,100),font,4,(10,56,167)) #ADD_FONT_ON_IMAGE
cv2.line(image,(0,0),(400,400),(255,0,0),5) #cross_line_on_image
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()