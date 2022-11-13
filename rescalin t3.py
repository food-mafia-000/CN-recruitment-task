import cv2
import numpy as np

def ups(img):

    cv2.imshow("Original Image",image)
    cv2.imshow("Previous Image",resized)

    wid=wid+w
    hgt=hgt+h
    points=(wid,hgt)
    resized=cv2.resize(image,points,interpolation=cv2.INTER_LINEAR)
    cv2.imshow("DownScaled resized image",resized)
    cv2.waitKey()


def dons(img):
    cv2.imshow("Original Image",image)
    cv2.imshow("Previous Image",resized)
    
    wid=wid-w
    hgt=hgt-h
    points=(wid,hgt)
    resized=cv2.resize(resized,points,interpolation=cv2.INTER_LINEAR)
    cv2.imshow("DownScaled resized image",resized)
    cv2.waitKey()

print("*Please make sure thatimage is in same folder as code")
print(" Enter 0 if want to use default image")
path=str(input("Enter the name of the image: "))


if (path=="0"):
    image=cv2.imread("download.jpg")
else:
    image=cv2.imread(path)
#image=cv2.imread("download.jpg")
cv2.imshow("Original Image",image)
resized=image
wid = image.shape[1]
hgt = image.shape[0]
w=wid/10
h=hgt/10

t=0
while( t==0 ):
    print("Press 1 to upscale image")
    print("Press 2 to downscale image")
    print("Press 0 to Exit")
    
    p=int(input("Enter your Choice: "))
    cv2.destroyAllWindows()
    # match p:
    #     case 0:
    #         break
    #     case 1:
    #         ups(image)
    #     case 2:
    #         dons(image)
    if (p==1):
        ups(image)
    elif(p==2):
        dons(image)
    else:
        break
print(" The program has ended ")
print(" thank youu for using ")