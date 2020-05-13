import cv2
import numpy as np

back_img = np.zeros((480, 640, 3), np.uint8)

def main():
    def Magic(frame1):
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Red Color Range
        low = np.array([0,120,70])
        high = np.array([10,255,255])
        mask1 = cv2.inRange(hsv,low,high)
        low = np.array([170,120,70])
        high = np.array([180,255,255])
        mask2 = cv2.inRange(hsv,low,high)
        mask = mask1 + mask2

        mask_inv = cv2.bitwise_not(mask)
        img1_bg = cv2.bitwise_and(back_img, back_img, mask=mask)
        img2_fg = cv2.bitwise_and(frame1, frame1, mask=mask_inv)
        dst = cv2.add(img1_bg, img2_fg)
        cv2.imshow("Invisible Frame", dst)
        cv2.imshow("Original Frame", frame1)
        
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
        global back_img
        back_img = np.copy(frame)

    else:
        ret = False
        
    while ret:
        ret, frame = cap.read()
        test1 = Magic(frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()
