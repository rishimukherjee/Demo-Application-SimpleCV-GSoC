# copyright: Rishi Mukherjee
from SimpleCV import *
import cv2
import cv
import numpy as np

img1 = Image("s.jpg")
img2 = Image("t.jpg")
dst = Image((2000, 1600))
dst = dst.blit(img1)
ofimg = img1.findKeypointMatch(img2)
homo = ofimg[1]
eh = dst.getMatrix()
x = Image(cv2.warpPerspective(np.array((img2.getMatrix())), homo, (eh.rows, eh.cols+300), np.array(eh), cv.INTER_CUBIC))
x = x.blit(img1, alpha=0.4)
x.save("rishi1.jpg")

##visit http://imgur.com/a/lrGw4#0 to view the results.