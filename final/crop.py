import cv2
import numpy as np 
import sys
impath="/home/bharat/Downloads/i.jpg"
np.set_printoptions(threshold=sys.maxsize)
img=cv2.imread(impath,0)
cnt=0
c1=0
c2=0
x2,x1,y2,y1=0,1000,0,1000
for i in range(1,img.shape[0]):
	for j in range(1,img.shape[1]):
		if(img[i][j]<100):

			ok = True
			for k in range(1):
				if img[i-k][j] > 100:
					ok = False
					break
			if ok:
				x1=min(x1,i)
				x2=max(x2,i)

			ok = False
			for k in range(1):
				if img[i][j-k] > 100:
					ok = False
					break

			if ok:
				y1=min(y1,j)			
				y2=max(y2,j)			
			cnt+=1
img[x1:x2,y1:y2]=0
cv2.imwrite("out.png",img)
# cv2.imshow("out.png")
print(cnt,img.shape)
print(x1,x2,y1,y2)