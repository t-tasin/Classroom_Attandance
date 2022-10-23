import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'Member'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

#Read all images and create array of Images and Names
for cl in myList:
    currentImage = cv2.imread(f'{path}/{cl}')
    images.append(currentImage)
    classNames.append(os.path.splitext(cl)[0])

#print(classNames)

#Converting image color to RGB and create an array of encoded images
def find_encodings(images):
    encode_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list

#Take the time frame, when the face showed up on camera and write that in a csv file
def Face_TimeFrame(name):
    with open('WhenYouShowUp.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        print(myDataList)
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dateString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {dateString}')

encode_list_known = find_encodings(images)
print('Encoding Completed')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgSmall = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(imgSmall)
    encodeCurrentFrame = face_recognition.face_encodings(imgSmall, facesCurrentFrame)

    for encodeFace, faceLocation in zip(encodeCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encode_list_known, encodeFace)
        faceDistance = face_recognition.face_distance(encode_list_known, encodeFace)
        print(faceDistance)
        matchIndex = np.argmin(faceDistance)

        if faceDistance[matchIndex] < 0.50:
            name = classNames[matchIndex].upper()
            Face_TimeFrame(name)
        else:
            name = 'UNKNOWN'
        y1, x2, y2, x1 = faceLocation
        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
        cv2.rectangle(img, (x1,y1),(x2,y2), (255,0,0), 2)
        cv2.rectangle(img, (x1,y2-50),(x2,y2),(255,0,0), cv2.FILLED)
        cv2.putText(img, name, (x1+20,y2-6), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255,255,255), 3)
        Face_TimeFrame(name)

    cv2.imshow('Camera', img)
    i = cv2.waitKey(10) & 0xff #Press 'ESC' for exiting video
    if i == 27:
        break