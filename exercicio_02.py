import cv2
import numpy as np

img_tomate = cv2.imread("tomate.png")

blur = cv2.blur(img_tomate, (11,11))
cv2.imshow("Imagem com Blur", blur)

img_tomate_hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
cv2.imshow("tomate_hsv", img_tomate_hsv)

v1 = cv2.inRange(img_tomate_hsv, (0, 50, 200), (10, 255, 255))
v2 = cv2.inRange(img_tomate_hsv, (160, 50, 200), (179, 255, 255))
pena = cv2.add(v1,v2)
img_tomate_pena = cv2.bitwise_and(img_tomate_hsv, img_tomate_hsv, mask = pena)
cv2.imshow("base_pena", img_tomate_pena)

img_tomate_result = cv2.cvtColor(img_tomate_pena, cv2.COLOR_HSV2BGR)
cv2.imwrite('resposta_02.jpg', img_tomate_result)
cv2.imshow("resultado final", img_tomate_result)

cv2.waitKey()
cv2.destroyAllWindows()