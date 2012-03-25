from SimpleCV import *

#import the images
img1 = Image("t.jpg")
img2 = Image("s.jpg")

#find the keypoints
ofimg = img1.findKeypointMatch(img2)


#After this I found all the coordinates of the returned box on the image.

#coordinates of the box drawn by ofimg
x = ofimg[0].topLeftCorner()[0]
y = ofimg[0].topLeftCorner()[1]
w = ofimg[0].width
h = ofimg[0].height

#Then I cropped the image and saved into another variable and also cropped the left and right of the panorama from both the images accordingly.

#cropped image from main image
cropped_img = img1.crop(x, y, w, h)

#the left side of the panorama
left = img2.crop(0, 0, img1.width-w, h)

#the right side of the panorama
right = img1.crop(ofimg[0].topRightCorner()[0], 0, img1.width-ofimg[0].topRightCorner()[0], img1.height)

#Now I joined the left and main cropped image and saved into a temporary variable, followed by the final Image.

#a temporary image
temp = left.sideBySide(cropped_img)

#the final image
joined = temp.sideBySide(right)
joined.show()
