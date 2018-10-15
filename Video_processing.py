import cv2,time

video = cv2.VideoCapture(0)   # 0 for built in web cam. 1 for exteranl web cam . for video pass path

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
number_of_frames_per_second=0
while True:
    number_of_frames_per_second=number_of_frames_per_second+1
    check, frame= video.read()
    #time.sleep(3)
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05, minNeighbors=5)

    for x,y,w,h in face:
        gray_img= cv2.rectangle(gray_img,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow("CapturedVideo",gray_img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(number_of_frames_per_second)
video.release()
cv2.destroyAllWindows

#capturing approx 30 frames per second
