# copyright: Rishi Mukherjee
from SimpleCV import *

img1 = Image("s.jpg")
img2 = Image("t.jpg")
dst = Image((2000, 1600))
ofimg = img1.findKeypointMatch(img2) #find the keypoints
homo = ofimg[1] #the homography matrix
eh = dst.getMatrix()
#transform the image
x = Image(cv2.warpPerspective(np.array((img2.getMatrix())), homo, (eh.rows, eh.cols+300), np.array(eh), cv.INTER_CUBIC), colorSpace=ColorSpace.RGB).toBGR()
#blit the img1 now on coordinate (0, 0)
x = x.blit(img1, alpha=0.4)
x.save("rishi1.jpg")
##visit http://imgur.com/Xf7WS to view the results.