import cv2

img = cv2.imread('sinmina3.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('sinmina_LOVE', img)
cv2.imshow('sinmina-gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
