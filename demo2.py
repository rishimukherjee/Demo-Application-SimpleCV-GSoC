from SimpleCV import *
import cv2
import cv
import numpy as np

img1 = Image("s.jpg")
img2 = Image("t.jpg")
src = img1.copy()
dst = Image((1600, 1200))
ofimg = img1.findKeypointMatch(img2)
homo = ofimg[1]
eh = dst.getMatrix()
j = cv2.warpPerspective(np.array((img2.getMatrix())), homo, (eh.rows, eh.cols), np.array(eh), cv.INTER_CUBIC)
poster = Image((3200, 1600))
poster = poster.blit(img1, pos=(0, 250))
poster = poster.blit(Image(j), alpha=0.3, pos=(250, 10))
poster.save("trying.jpg")