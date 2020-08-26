import cv2

img = cv2.imread('sinmina3.jpeg')
print("width: {} pixels".format(img.shape[1]))
print("heigh: {} pixels".format(img.shape[0]))
print("channels: {} ".format(img.shape[2]))

cv2.imshow('sinmina_LOVE', img)

(b,g,r) = img[0, 0]
print("Pixel as (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

dot = img[50:100, 50:100]
img[50:100, 50:100] = (0, 0, 255)

cv2.rectangle(img,(150,50), (200,100), (0,255,0), 5)
cv2.circle(img, (275, 75), 25, (0, 255, 255), 1)
cv2.line(img, (350, 100), (400, 100), (255, 0, 0), 5)
cv2.putText(img, 'sinmina_LOVE', (450,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)

cv2.imshow('sinmina-final', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
