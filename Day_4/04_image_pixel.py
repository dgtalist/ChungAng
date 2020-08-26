import cv2

img = cv2.imread('sinmina3.jpeg')
print("width: {} pixels".format(img.shape[1]))
print("heigh: {} pixels".format(img.shape[0]))
print("channels: {} ".format(img.shape[2]))

cv2.imshow('sinmina_LOVE', img)

(b,g,r) = img[0, 0]
print("Pixel as (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

dot = img[50:100, 50:100]
cv2.imshow("sinmin-dot", dot)

img[50:100, 50:100] = (0, 0, 255)
cv2.imshow("dot", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
