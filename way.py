import cv2

img = cv2.imread('img/aquarium.jpg')
rainbow = cv2.imread('img/rainbow.png')

cv2.namedWindow('ui')
cv2.createTrackbar('h_min', 'ui', 0, 180, )