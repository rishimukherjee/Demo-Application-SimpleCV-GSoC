# copyright: Rishi Mukherjee
from SimpleCV import *
import cv2
import cv
import numpy

img1 = Image("s.jpg")
img2 = Image("t.jpg")
dst = Image((2000, 1600))
fs = img1.findKeypointMatch(img2)
homo = fs[0].getHomography()
eh = dst.getMatrix()
x = Image(cv2.warpPerspective(np.array((img2.getMatrix())), homo, (eh.rows, eh.cols+300), np.array(eh), cv2.INTER_CUBIC), colorSpace=ColorSpace.RGB).toBGR()
x = x.blit(img1, alpha=1.0)