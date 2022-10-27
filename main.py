import sys
import Update
from ReverseSearch import UploadImage, SearchImage  
import numpy as np
import cv2
import face_recognition
import json


ui = UploadImage()
si = SearchImage()
# link = ui.upload("rekha.jpeg")
# link

known_face_names,  known_face_encodings = Update.update()

faceCascade = cv2.CascadeClassifier('Models/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,1000) # set Width
cap.set(4,720) # set Height
while True:
    ret, img = cap.read()
    # img = cv2.flip(img)
    img = np.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor = 1.2,
        minNeighbors = 8,
        minSize = (10, 10)
        # maxSize = (480,480)
    )
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        roi_gray = gray[y:y+h+1, x:x+w+1]
        roi_color = img[y:y+h+1, x:x+w+1]
        
        cv2.imwrite("catch.jpg", roi_color)

        # Load an image with an unknown face
        # unknown_image = face_recognition.load_image_file("catch.jpg")

        # Find all the faces and face encodings in the unknown image
        unknown_image = roi_color
        # unknown_image = roi_gray
        # print(type(face_image))
        # face_locations = face_recognition.face_locations(unknown_image)

        face_encodings = face_recognition.face_encodings(unknown_image)
        if(len(face_encodings) >= 1):
            face_encodings = face_encodings[0]

            # print(face_encodings)
            # print(known_face_encodings)
            matches = face_recognition.compare_faces(known_face_encodings, face_encodings, tolerance=0.62)

            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encodings)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # font
            font = cv2.FONT_HERSHEY_SIMPLEX
            
            # org
            org = (x , y + h + 40)
            
            # fontScale
            fontScale = 1.2
            
            # Blue color in BGR
            color = (255, 255, 150)
            
            # Line thickness of 2 px
            thickness = 2
            
            # Using cv2.putText() method
            image = cv2.putText(img, name, org, font, 
                            fontScale, color, thickness, cv2.LINE_AA)



    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
    elif k == ord('f'):
        link = ui.upload("catch.jpg")
        data = si.search(link)
        with open("temp.json", 'w') as f:
            f.write(json.dumps(data, indent = 4))
cap.release()
cv2.destroyAllWindows()