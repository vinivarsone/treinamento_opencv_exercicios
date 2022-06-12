import cv2
import numpy as np

img_base = cv2.imread("base.png")

#blur = cv2.blur(img_base, (11,11))
median = cv2.medianBlur(img_base, 11)
#guassian = cv2.GaussianBlur(img_base, (11,11), 0)

#cv2.imshow("base", img_base)
#cv2.imshow("base_blur", blur)
cv2.imshow("base_median", median)
#cv2.imshow("base_guassiana", guassian)

img_base_hsv = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)
cv2.imshow("base_hsv", img_base_hsv)

v1 = cv2.inRange(img_base_hsv, (0, 50, 200), (10, 255, 255))
v2 = cv2.inRange(img_base_hsv, (160, 50, 200), (179, 255, 255))
pena = cv2.add(v1,v2)
img_base_pena = cv2.bitwise_and(img_base_hsv, img_base_hsv, mask = pena)

cv2.imshow("base_pena", img_base_pena)

cv2.waitKey()
cv2.destroyAllWindows()



