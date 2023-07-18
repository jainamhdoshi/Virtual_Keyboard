import cv2
import keyboard_module as htm
import pyautogui

    
def keyboard():
    cap = cv2.VideoCapture(0)
    wCam, hCam = 640, 480
    cap.set(3, wCam)
    cap.set(4, hCam)

    detector = htm.handDetector(detectionCon=0.7, maxHands=2)

    r1_reset = True
    r2_reset = True
    r3_reset = True
    r4_reset = True
    l1_reset = True
    l2_reset = True
    l3_reset = True
    l4_reset = True
    shift_press = False

    while True:
        success, img = cap.read()
        img_flipped = cv2.flip(img, 1)
        img = detector.findHands(img_flipped)
        lmList0, box0 = detector.findPosition(img, handNo=0, draw_circle=True, draw_box=False)
        lmList1, box1 = detector.findPosition(img, handNo=1, draw_circle=True, draw_box=False)

        fingers_r = []
        fingers_l = []

        def rl_detector(inp_list):
            if inp_list[4][1] < inp_list[20][1]:
                return 0
            if inp_list[4][1] > inp_list[20][1]:
                return 1

        if len(lmList0) != 0:
            area0 = (box0[2] - box0[0]) * (box0[3] - box0[1]) // 100

            if area0 > 150:
                fingers0 = detector.fingersUp(lmList0)
                if rl_detector(lmList0) == 0:
                    fingers_r = fingers0
                if rl_detector(lmList0) == 1:
                    fingers_l = fingers0

        if len(lmList1) != 0:
            area1 = (box1[2] - box1[0]) * (box1[3] - box1[1]) // 100

            if area1 > 150:
                fingers1 = detector.fingersUp(lmList1)
                if rl_detector(lmList1) == 0:
                    fingers_r = fingers1
                if rl_detector(lmList1) == 1:
                    fingers_l = fingers1

        if len(fingers_r) != 0 and len(fingers_l) != 0:
            if fingers_r[1:2] == [1]:
                r1_reset = True
            if fingers_r[2:3] == [1]:
                r2_reset = True
            if fingers_r[3:4] == [1]:
                r3_reset = True
            if fingers_r[4:5] == [1]:
                r4_reset = True
            if fingers_l[1:2] == [1]:
                l1_reset = True
            if fingers_l[2:3] == [1]:
                l2_reset = True
            if fingers_l[3:4] == [1]:
                l3_reset = True
            if fingers_l[4:5] == [1]:
                l4_reset = True

            if fingers_r[0:1] == [1] and fingers_l[0:1] == [1]:
                if fingers_l[1:5] == [1, 1, 1, 0] and l4_reset:
                    if shift_press:
                        pyautogui.press("1")
                    else:
                        pyautogui.press("a")
                    l4_reset = False

                if fingers_l[1:5] == [1, 1, 0, 1] and l3_reset:
                    if shift_press:
                        pyautogui.press("S")
                    else:
                        pyautogui.press("s")
                    l3_reset = False

                if fingers_l[1:5] == [1, 0, 1, 1] and l2_reset:
                    if shift_press:
                        pyautogui.press("D")
                    else:
                        pyautogui.press("d")
                    l2_reset = False

                if fingers_l[1:5] == [0, 1, 1, 1] and l1_reset:
                    if shift_press:
                        pyautogui.press("F")
                    else:
                        pyautogui.press("f")
                    l1_reset = False

                if fingers_r[1:5] == [0, 1, 1, 1] and r1_reset:
                    if shift_press:
                        pyautogui.press("H")
                    else:
                        pyautogui.press("h")
                    r1_reset = False

                if fingers_r[1:5] == [1, 0, 1, 1] and r2_reset:
                    if shift_press:
                        pyautogui.press("J")
                    else:
                        pyautogui.press("j")
                    r2_reset = False

                if fingers_r[1:5] == [1, 1, 0, 1] and r3_reset:
                    if shift_press:
                        pyautogui.press("K")
                    else:
                        pyautogui.press("k")
                    r3_reset = False

                if fingers_r[1:5] == [1, 1, 1, 0] and r4_reset:
                    if shift_press:
                        pyautogui.press("L")
                    else:
                        pyautogui.press("l")
                    r4_reset = False

            if fingers_r[0:1] == [0] and fingers_l[0:1] == [1]:
                if fingers_l[1:5] == [1, 1, 1, 0] and l4_reset:
                    if shift_press:
                        pyautogui.press("Q")
                    else:
                        pyautogui.press("q")
                    l4_reset = False

                if fingers_l[1:5] == [1, 1, 0, 1] and l3_reset:
                    if shift_press:
                        pyautogui.press("W")
                    else:
                        pyautogui.press("w")
                    l3_reset = False

                if fingers_l[1:5] == [1, 0, 1, 1] and l2_reset:
                    if shift_press:
                        pyautogui.press("E")
                    else:
                        pyautogui.press("e")
                    l2_reset = False

                if fingers_l[1:5] == [0, 1, 1, 1] and l1_reset:
                    if shift_press:
                        pyautogui.press("R")
                    else:
                        pyautogui.press("r")
                    l1_reset = False

                if fingers_r[1:5] == [0, 1, 1, 1] and r1_reset:
                    if shift_press:
                        pyautogui.press("Y")
                    else:
                        pyautogui.press("y")
                    r1_reset = False

                if fingers_r[1:5] == [1, 0, 1, 1] and r2_reset:
                    if shift_press:
                        pyautogui.press("U")
                    else:
                        pyautogui.press("u")
                    r2_reset = False

                if fingers_r[1:5] == [1, 1, 0, 1] and r3_reset:
                    if shift_press:
                        pyautogui.press("I")
                    else:
                        pyautogui.press("i")
                    r3_reset = False

                if fingers_r[1:5] == [1, 1, 1, 0] and r4_reset:
                    if shift_press:
                        pyautogui.press("O")
                    else:
                        pyautogui.press("o")
                    r4_reset = False

            if fingers_r[0:1] == [1] and fingers_l[0:1] == [0]:
                if fingers_l[1:5] == [1, 1, 1, 0] and l4_reset:
                    if shift_press:
                        pyautogui.press("Z")
                    else:
                        pyautogui.press("z")
                    l4_reset = False

                if fingers_l[1:5] == [1, 1, 0, 1] and l3_reset:
                    if shift_press:
                        pyautogui.press("X")
                    else:
                        pyautogui.press("x")
                    l3_reset = False

                if fingers_l[1:5] == [1, 0, 1, 1] and l2_reset:
                    if shift_press:
                        pyautogui.press("C")
                    else:
                        pyautogui.press("c")
                    l2_reset = False

                if fingers_l[1:5] == [0, 1, 1, 1] and l1_reset:
                    if shift_press:
                        pyautogui.press("V")
                    else:
                        pyautogui.press("v")
                    l1_reset = False

                if fingers_r[1:5] == [0, 1, 1, 1] and r1_reset:
                    if shift_press:
                        pyautogui.press("B")
                    else:
                        pyautogui.press("b")
                    r1_reset = False

                if fingers_r[1:5] == [1, 0, 1, 1] and r2_reset:
                    if shift_press:
                        pyautogui.press("N")
                    else:
                        pyautogui.press("n")
                    r2_reset = False

                if fingers_r[1:5] == [1, 1, 0, 1] and r3_reset:
                    if shift_press:
                        pyautogui.press("M")
                    else:
                        pyautogui.press("m")
                    r3_reset = False

                if fingers_r[1:5] == [1, 1, 1, 0] and r4_reset:
                    if shift_press:
                        pyautogui.press("P")
                    else:
                        pyautogui.press("p")
                    r4_reset = False

            if fingers_r[0:1] == [0] and fingers_l[0:1] == [0]:
                if fingers_l[1:5] == [1, 1, 1, 0] and l4_reset and not shift_press:
                    shift_press = True
                    l4_reset = False

                if fingers_l[1:5] == [1, 1, 1, 0] and l4_reset and shift_press:
                    shift_press = False
                    l4_reset = False

                if fingers_l[1:5] == [1, 1, 0, 1] and l3_reset:
                    if shift_press:
                        pyautogui.press("=")
                    else:
                        pyautogui.press("enter")
                    l3_reset = False

                if fingers_l[1:5] == [1, 0, 1, 1]:
                    if shift_press:
                        pyautogui.press("delete")
                    else:
                        pyautogui.press("backspace")
                    l2_reset = False

                if fingers_l[1:5] == [0, 1, 1, 1] and l1_reset:
                    if shift_press:
                        pyautogui.press("T")
                    else:
                        pyautogui.press("t")
                    l1_reset = False

                if fingers_r[1:5] == [0, 1, 1, 1] and r1_reset:
                    if shift_press:
                        pyautogui.press("G")
                    else:
                        pyautogui.press("g")
                    r1_reset = False

                if fingers_r[1:5] == [1, 0, 1, 1] and r2_reset:
                    if shift_press:
                        pyautogui.press(":")
                    else:
                        pyautogui.press(",")
                    r2_reset = False

                if fingers_r[1:5] == [1, 1, 0, 1] and r3_reset:
                    if shift_press:
                        pyautogui.press('?')
                    else:
                        pyautogui.press(".")
                    r3_reset = False

                if fingers_r[1:5] == [1, 1, 1, 0] and r4_reset:
                    if not shift_press:
                        pyautogui.press("space")
                    r4_reset = False

        cv2.imshow("Image", img)
        cv2.waitKey(1)

keyboard()
