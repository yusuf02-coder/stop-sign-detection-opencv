import cv2
import numpy as np
import os

input_folder = "stop_sign_dataset"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

for image_name in os.listdir(input_folder):

    image_path = os.path.join(input_folder, image_name)

    image = cv2.imread(image_path)

    if image is None:
        continue

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Kırmızı için iki HSV aralığı gerekir
    lower_red1 = np.array([0,120,70])
    upper_red1 = np.array([10,255,255])

    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    kernel = np.ones((5,5),np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernel)

    contours, _ = cv2.findContours(mask,
                                   cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area < 500:
            continue

        x,y,w,h = cv2.boundingRect(cnt)

        cx = x + w//2
        cy = y + h//2

        cv2.rectangle(image,
                      (x,y),
                      (x+w,y+h),
                      (0,255,0),
                      3)

        cv2.circle(image,
                   (cx,cy),
                   5,
                   (255,0,0),
                   -1)

        cv2.putText(image,
                    "STOP",
                    (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,255,0),
                    2)

        print(f"{image_name} --> Merkez = ({cx}, {cy})")

    save_path = os.path.join(output_folder,image_name)

    cv2.imwrite(save_path,image)

print("Tamamlandi.")