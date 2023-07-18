import cv2
import mediapipe as mp
import time
import math



class handDetector:
    def __init__(self, mode=False, maxHands=2, modelC=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelC = modelC
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelC, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo, draw_circle=True, draw_box=False, colour=(255, 0, 0)):
        xList = []
        yList = []
        lmList = []
        box = []
        try:
            if self.results.multi_hand_landmarks:
                myHand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy, cz = int(lm.x * w), int(lm.y * h), int(lm.z * h)
                    lmList.append([id, cx, cy, cz])
                    xList.append(cx)
                    yList.append(cy)
                    if draw_circle:
                        cv2.circle(img, (cx, cy), 7, colour, cv2.FILLED)
                x_min, x_max = min(xList), max(xList)
                y_min, y_max = min(yList), max(yList)
                box = [x_min, y_min, x_max, y_max]

                if draw_box:
                    cv2.rectangle(img, (box[0]-20, box[1]-20),
                                  (box[2]+20, box[3]+20), (0, 255, 0), 2)
        except:
            pass

        return lmList, box

    def fingersUp(self, inp_list):
        fingers = []

        # Right Thumb
        if inp_list[4][1] > inp_list[20][1]:
            if inp_list[self.tipIds[0]][1] > inp_list[self.tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Left Thumb
        if inp_list[4][1] < inp_list[20][1]:
            if inp_list[self.tipIds[0]][1] < inp_list[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # 4 fingers
        for id in range(1, 5):
            if inp_list[self.tipIds[id]][2] < inp_list[self.tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def findDistance(self, p1, p2, img, draw=True):
        x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
        x2, y2 = self.lmList[p2][1], self.lmList[p2][2]

        length = math.hypot(x2 - x1, y2 - y1)

        return length, img, [x1, y1, x2, y2]

def main():
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
