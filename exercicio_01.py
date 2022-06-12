import cv2
import numpy as np

img_base = cv2.imread("base.png")

median = cv2.medianBlur(img_base, 11)
cv2.imshow("base_median", median)

img_base_hsv = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)
cv2.imshow("base_hsv", img_base_hsv)

v1 = cv2.inRange(img_base_hsv, (0, 0, 0), (5, 255, 200))
v2 = cv2.inRange(img_base_hsv, (175, 190, 50), (255, 255, 200))
mascara = cv2.add(v1,v2)
img_base_mascara = cv2.bitwise_and(img_base_hsv, img_base_hsv, mask = mascara)
cv2.imshow("base_mascara", img_base_mascara)

img_base_result = cv2.cvtColor(img_base_mascara, cv2.COLOR_HSV2BGR)
cv2.imwrite('resposta_01.jpg', img_base_result)
cv2.imshow("resultado final", img_base_result)

cv2.waitKey()
cv2.destroyAllWindows()