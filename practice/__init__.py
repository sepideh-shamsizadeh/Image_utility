import cv2

path = '/home/sepid/Desktop/p.png'
image = cv2.imread(path)
cv2.namedWindow('image', flags=cv2.WINDOW_FREERATIO)
cv2.resizeWindow('image', 1500, 2000)
cv2.imshow('image', image)
cv2.waitKey(0)
