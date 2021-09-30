import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpdraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


while True:
    succes, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print("-id--x---y\n",id,cx,cy)

                cv2.circle(img,(cx,cy), 5, (155,255,90), cv2.FILLED)
                if id == 0:
                    cv2.circle(img,(cx,cy),8,(0,0,255),cv2.FILLED)

 

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (580,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)

    cv2.imshow('image', img)
    cv2.waitKey(1)