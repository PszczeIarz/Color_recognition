import cv2

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = camera.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height/2)

    #PICK  pixel value
    pixel_center = frame[cy, cx]
    hue_value = pixel_center[0]

    if hue_value < 5 :
        color = "czarny 5"
    elif hue_value < 22:
        color = "Pomarańczowy 22"
    elif hue_value < 33:
        color = "Żółty  33"
    elif hue_value < 78:
        color = "Zielony 78"
    elif hue_value < 131:
        color = "Fioletowy 131"
    elif hue_value < 170:
        color = "Czerwony"


    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.putText(frame, color, (10, 70), 0, 1.5, (b,g,r),2)
    cv2.circle(frame, (cx, cy), 5, (255,255, 255),3)  #

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

camera.relase()
cv2.destroyAllWindows()

