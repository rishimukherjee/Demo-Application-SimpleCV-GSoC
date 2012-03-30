from SimpleCV import *
import cv2
import cv
import numpy as np

img1 = Image("s.jpg")
img2 = Image("t.jpg")
src = img1.copy()
dst = Image((1600, 1200))
ofimg = img2.findKeypointMatch(img1)
x = ofimg[0].topLeftCorner()[0]
y = ofimg[0].topLeftCorner()[1]
array = ofimg[1]
eh = dst.getMatrix()
j = cv2.warpPerspective(np.array((img2.getMatrix())), array, (eh.rows*2, eh.cols*2), np.array(eh), cv.INTER_CUBIC)
np.array((img1.getMatrix()))
Image(j).save("trying.jpg")
final = cv.CreateMat(eh.cols*2+eh.cols, eh.rows*2, cv.CV_8UC3)
roi1 = cv.GetSubRect(final, (0, 0, eh.rows, eh.cols))
roi2 = cv.GetSubRect(final, (0, 0, eh.rows*2, eh.cols*2))
final = np.asarray(final)
roi1 = np.asarray(roi1)
roi2 = np.asarray(roi2)
warpImage2 = Image(final).blit(Image(j))
mImg1 = Image("x.jpg").blit(img1)
