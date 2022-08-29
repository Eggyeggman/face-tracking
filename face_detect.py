import cv2

img = cv2.imread("4f.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray,1.1,5)
print(len(faces))

#for (x,y,w,h) in faces:
#       cv2.rectangle(img,(x,y),(x+w,y+h),(50,50,50),2)
#       crop = img[y:y+h,x:x+w]
#       cv2.imwrite("when_the_sus.jpg",crop)
             
cv2.imshow('imposter',img)
cv2.waitKey(0)



