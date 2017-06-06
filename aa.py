import cv2
import gtk, pygtk

fname = 'jh.jpg'

original = cv2.imread(fname, cv2.IMREAD_COLOR)
gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
unchange = cv2.imread(fname, cv2.IMREAD_UNCHANGED)

cv2.startWindowThread()
cv2.namedWindow("Original")
cv2.imshow('Original', original)
cv2.waitKey(0)
cv2.imshow('Gray', gray)
cv2.waitKey(0)
cv2.imshow('Unchange', unchange)

cv2.waitKey(0)
cv2.destroyAllWindows()
