import numpy as np
import pandas as pd
from Database import init
from Face_Encoding import faceEncoding


def update():
    known_face_names, _ , known_face_path = init()

    known_face_names = np.asarray(known_face_names)
        
    faceEncodings = [faceEncoding(image_path = path) for path in known_face_path]
    faceEncodings = np.asarray(faceEncodings)
    # faceEncodings = np.reshape(faceEncodings, newshape = (7, 128))
    return known_face_names, faceEncodings
    # print(faceEncodings.shape)
    # print(faceEncodings[0])
        
    # data_sheet = pd.DataFrame(faceEncodings, columns = range(0,128))
    # data_sheet["names"] = known_face_names
    # data_sheet.to_csv("face_encoding_data.csv")

