#Find links to images in the README.
import time
y = time.time()
import cv2
import cv
from SimpleCV import *
import numpy as np

template = Image("t.jpg")
img = Image("s.jpg")
dst = Image((1600, 1200))
thisMask = Image((2400, 3200))
quality = 500.0
skp, sd = img._getRawKeypoints(quality)
tkp, td = template._getRawKeypoints(quality)
template_points = float(td.shape[0])
sample_points = float(sd.shape[0])
magic_ratio = 1.00
if ( sample_points > template_points ):
    magic_ratio = sample_points/template_points
idx, dist = img._getFLANNMatches(sd, td)
lengthOfIdx = len(idx)
p = dist[:, 0]
result = p*magic_ratio < 0.2
pr = result.shape[0]/float(dist.shape[0])
if pr >0.4 and len(result) > 4:
    lhs = []
    rhs = []
    for i in range(lengthOfIdx):
        if result[i]:
            lhs.append((tkp[i].pt[0], tkp[i].pt[1]))
            rhs.append((skp[idx[i]].pt[1], skp[idx[i]].pt[0]))
    rhs_pt = np.array(rhs)
    lhs_pt = np.array(lhs)
    homography = []
    (homography, mask) = cv2.findHomography(lhs_pt, rhs_pt, cv2.RANSAC, ransacReprojThreshold=1.0)    
eh = dst.getMatrix()
ee = cv2.warpPerspective(np.array((img.getMatrix())), homography, (eh.rows*2, eh.cols*2), np.array(eh))
Image(ee).save("hehe.jpg")
white = 255.0, 255.0, 255.0
gsThisImage = img.getMatrix()[:]
for i in range(gsThisImage.rows):
    for j in range(gsThisImage.cols):
        gsThisImage[i, j] = white
cv2.cvtColor(np.array(gsThisImage), cv.CV_BGR2GRAY, np.array(gsThisImage))
xx = cv2.warpPerspective(np.array(gsThisImage), homography, (eh.rows, eh.cols), np.array(thisMask.getMatrix()))
thisMask = Image(xx)
kk=Image(ee).blit(template, mask=thisMask, pos=(230, 260))
kk.show()
kk.save("hoho.jpg")
