import numpy as np
import face_recognition



def faceEncoding(image_path, image = None):

    if(image == None):
        image = face_recognition.load_image_file(image_path)
     
    # face_location = face_recognition.face_locations(image)

    face_encoding = face_recognition.face_encodings(image, num_jitters = 1)[0]

    return face_encoding
