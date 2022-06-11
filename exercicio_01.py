import cv2
import numpy as np

img_base = cv2.imread("base.png")

cv2.imshow("base", img_base)

cv2.waitKey()
cv2.destroyAllWindows()

