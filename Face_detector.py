import cv2

facetrain = cv2.CascadeClassifier('frintalface.xml')

# amg = cv2.imread('wera.jpg')
webcam = cv2.VideoCapture(0)

while True:
    
    sucessful_frame_read, frame = webcam.read()
    
    gray_man = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    trainmike = facetrain.detectMultiScale(gray_man)
    
    for (x, y, w, h) in  trainmike:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (225, 225,0), 2)
    
    cv2.imshow('i be dead', frame)
    cv2.waitKey(1)

# gray_man = cv2.cvtColor(webcam, cv2.COLOR_BGR2GRAY)

# trainmike = facetrain.detectMultiScale(gray_man)



# for (x, y, w, h) in  trainmike:
#         cv2.rectangle(amg, (x, y), (x+w, y+h), (225, 225,0), 2)

# print(trainmike)

# cv2.imshow('i be dead', amg)
# cv2.waitKey()

# print("code Completed")  