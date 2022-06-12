import cv2
import numpy as np

img_tomate = cv2.imread("tomate.png")

blur = cv2.blur(img_tomate, (11,11))
cv2.imshow("Imagem com Blur", blur)

img_tomate_hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
cv2.imshow("Imagem do Tomate em hsv", img_tomate_hsv)

v1 = cv2.inRange(img_tomate_hsv, (0, 50, 182), (20, 255, 255))
v2 = cv2.inRange(img_tomate_hsv, (160, 50, 200), (179, 255, 255))
mascara = cv2.add(v1,v2)
img_tomate_mascara = cv2.bitwise_and(img_tomate_hsv, img_tomate_hsv, mask = mascara)
cv2.imshow("Imagem do Tomate com a mascara", img_tomate_mascara)

img_tomate_BGR = cv2.cvtColor(img_tomate_mascara, cv2.COLOR_HSV2BGR)
img_tomate_gray = cv2.cvtColor(img_tomate_BGR, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem do Tomate em gray", img_tomate_gray)

#kernel = np.ones((48,48), np.uint8)
#tomate_dilation = cv2.dilate(img_tomate_gray, kernel, iterations = 1)

#kernel = np.ones((90,90), np.uint8)
#tomate_erode = cv2.erode(tomate_dilation, kernel, iterations = 1)

#kernel = np.ones((49,49), np.uint8)
#tomate_dilation = cv2.dilate(tomate_erode, kernel, iterations = 1)

contours, _ = cv2.findContours(img_tomate_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_tomate_contours = cv2.drawContours(img_tomate, contours, -1, (255, 0, 0), 3)

cv2.imwrite('Resposta_02.jpg', img_tomate_contours)
cv2.imshow("Imagem do Tomate com Contorno", img_tomate_contours)

cv2.waitKey()
cv2.destroyAllWindows()