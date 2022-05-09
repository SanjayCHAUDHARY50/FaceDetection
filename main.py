import cv2

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)

res, img = capture.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

faces = detect.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 3)
print(faces)
cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
capture.release()
cv2.destroyAllWindows()