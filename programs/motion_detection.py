# https://docs.opencv.org/3.4/d1/dc5/tutorial_background_subtraction.html
import cv2

cap = cv2.VideoCapture('Video.mov')

backSub = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = backSub.apply(frame)

    cv2.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv2.putText(frame, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgmask)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv2.destroyAllWindows()
