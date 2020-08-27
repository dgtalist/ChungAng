import cv2          # opencv를 사용하기 위해 cv2 라이브러리 import
import sys          # 시스템에서 명령어를 쓸 수 있도록
import math         # 수학정의, 어떤 수식이 개발되어 있는 것을 가져다 쓸 수 있게
import cv2 as cv    # as는 별칭으로 사용하겠다는 것
import numpy as np  # numpy는 수학적으로 통계낼 때 쓰는 라이브러리 (1)

cap = cv2.VideoCapture(0)         # 변수 cap = cv2 라이브러리 중 videocapture 사용, 0 : 데이터를 입력받는 구간 (2)

while (True):
    ret, src = cap.read()         # 캡쳐한 영상을 읽어오는 것, ret : return, src : 캡쳐한 이미지 (3)

    src = cv2.resize(src, (640, 360))           # resize로 영상의 크기를 640x360으로 줄임 (4)

    dst = cv.Canny(src, 50, 200, None, 3)       # canny는 영상을 인식할 수 있는 범주를 빼고 색을 반전

    cdst = cv.cvtColor(dst, cv.COLOR_BGR2RGB)   # RGB로 영상을 돌리면 흰색을 기점으로 색을 입혀서 컬러가 나온다. (5)
    cdstP = np.copy(cdst)                       # numpy는 배열처럼 생성되는데 np.copy하면 배열 그대로를 카피

    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv.line(cdst, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv.LINE_AA)

    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()