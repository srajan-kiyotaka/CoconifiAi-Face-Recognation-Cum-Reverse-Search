from deepface import DeepFace
import numpy as np
import cv2
import face_recognition
from PIL import Image, ImageDraw
from IPython.display import display
import mtcnn

from mtcnn.mtcnn import MTCNN
detector = MTCNN()


# Load a sample picture and learn how to recognize it.
srajan_image = face_recognition.load_image_file("Database/srajan/srajan.jpeg")
# print(type(obama_image))
srajan_face_encoding = face_recognition.face_encodings(srajan_image)[0]

# Load a second sample picture and learn how to recognize it.
atharva_image = face_recognition.load_image_file("Database/aniket/aniket.jpeg")
atharva_face_encoding = face_recognition.face_encodings(atharva_image)[0]

# Load a sample picture and learn how to recognize it.
sharan_image = face_recognition.load_image_file("Database/sharan/sharan.jpeg")
# print(type(obama_image))
sharan_face_encoding = face_recognition.face_encodings(sharan_image)[0]

# Load a second sample picture and learn how to recognize it.
vivek_image = face_recognition.load_image_file("Database/vivek/vivek.jpeg")
vivek_face_encoding = face_recognition.face_encodings(vivek_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    srajan_face_encoding,
    atharva_face_encoding,
    sharan_face_encoding,
    vivek_face_encoding
]
known_face_names = [
    "Srajan Chourasia",
    "atharva",
    "sharan",
    "vivek"
]

# for i in known_face_encodings:
#     print(f"face :::: {len(i)}")

print('Learned encoding for', len(known_face_encodings), 'images.')


faceCascade = cv2.CascadeClassifier('Models/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,1000) # set Width
cap.set(4,640) # set Height
while True:
    ret, img = cap.read()
    # img = cv2.flip(img)
    img = np.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector.detect_faces(img)

    # faces = faceCascade.detectMultiScale(
    #     gray,     
    #     scaleFactor=1.5,
    #     minNeighbors=5,     
    #     minSize=(20, 20)
    # )
    
    for face in faces:
        (x,y,w,h) = face["box"]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        # cv2.imwrite("catch.jpg", img)

        # Load an image with an unknown face
        # unknown_image = face_recognition.load_image_file("catch.jpg")

        # Find all the faces and face encodings in the unknown image
        unknown_image = roi_color
        # print(type(face_image))
        face_locations = face_recognition.face_locations(unknown_image)

        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
        if(len(face_encodings) >= 1):
            # result = DeepFace.verify(img, model_name =  "Facenet")
            # print(result)
            face_encodings = face_encodings[0]

            # print(face_encodings)
            # print(known_face_encodings)
            matches = face_recognition.compare_faces(known_face_encodings, face_encodings)

            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encodings)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # font
            font = cv2.FONT_HERSHEY_SIMPLEX
            
            # org
            org = (50, 50)
            
            # fontScale
            fontScale = 1
            
            # Blue color in BGR
            color = (255, 0, 0)
            
            # Line thickness of 2 px
            thickness = 2
            
            # Using cv2.putText() method
            image = cv2.putText(img, name, org, font, 
                            fontScale, color, thickness, cv2.LINE_AA)



    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
