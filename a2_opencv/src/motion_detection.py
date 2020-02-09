# from src: python motion_detection.py
# from a2_opencv: docker run --rm -v $(pwd)/src:/root opencv python ball_detection.py
# ref: https://docs.opencv.org/3.4/d1/dc5/tutorial_background_subtraction.html
import cv2

cap = cv2.VideoCapture('video/Video.mov')

backSub = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    if frame is None:
        break
    frame = cv2.transpose(frame)
    fgmask = backSub.apply(frame)

    cv2.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv2.putText(frame, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cv2.imwrite('images/output/FGMask.png', fgmask)
cap.release()
cv2.destroyAllWindows()
