import cv2
import numpy as np

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH,320) # set the width to 320 p
video.set(cv2.CAP_PROP_FRAME_HEIGHT,240) # set the height to 240 p

# The loop
while True:
  ret,frame = video.read()
  frame = cv2.flip(fqrame, -1)
  cv2.imshow("original",frame)

  key = cv2.waitKey(1)
  if key == 27:
    break

video.release()
cv2.destroyAllWindows()