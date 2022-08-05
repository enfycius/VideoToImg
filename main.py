import cv2

video = cv2.VideoCapture('file_name.MOV')

check, img = video.read()

count = 0

while check:
    cv2.imwrite('%d.png' % count, img)
    
    check, img = video.read()

    count += 1 