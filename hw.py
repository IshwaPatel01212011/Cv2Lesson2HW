import cv2
import os

bg = cv2.imread("Lesson 2/images/bg2.jpeg")
circle = cv2.imread("Lesson 2/images/circle.png")
triangle = cv2.imread("Lesson 2/images/triangle.jpeg")
girl = cv2.imread("Lesson 2/images/girl.jpeg")

resize = cv2.resize(circle, (640,640))
print(os.getcwd())
path = "/Users/ishwa/Documents/Jetlearn/OpenCV and Face Identification/Lesson 2/images"
os.chdir(path)
cv2.imwrite("circle.png",resize)

storing = cv2.addWeighted(circle, 0.5, triangle, 0.6, 1)
cv2.imshow("Adding to the Image", storing)
cv2.waitKey(0)

subtracting = cv2.subtract(circle, triangle)
cv2.imshow("Subtracting to the Image", subtracting)
cv2.waitKey(0)
