import numpy as np
import cv2

cap = cv2.VideoCapture(r"../data/tv_human/out/tv_human_interactions_videos/highFive_0011.avi")
while cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == True:
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
