import cv2

facetrain = cv2.CascadeClassifier('frintalface.xml')

amg = cv2.imread('thaks.jpg')

gray_man = cv2.cvtColor(amg, cv2.COLOR_BGR2GRAY)


trainmike = facetrain.detectMultiScale(gray_man)

(x, y, w, h) = trainmike[0]

cv2.rectangle(amg, (x, y), (x+w, y+h), (225, 225,0), 2)

print(trainmike)

cv2.imshow('i be dead', amg)
cv2.waitKey()

print("code Completed")  